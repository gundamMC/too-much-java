import subprocess
import os
import json

from django.db import models
from django.conf import settings
from django.utils import timezone

from users.models import Student

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    students = models.ManyToManyField(Student, related_name='courses', blank=True)

    def __str__(self):
        return str(self.name)


class CourseCode(models.Model):
    code = models.CharField(max_length=16)
    courses = models.ManyToManyField(Course, related_name='courses')

    def __str__(self):
        return str(self.code)


class Unit(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='units')

    def __str__(self):
        return str(self.name)


class Assignment(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, default=None, blank=True, null=True, related_name='assignments')
    due_date = models.DateTimeField()
    date = models.DateTimeField()

    points = models.PositiveSmallIntegerField()

    attempts = models.PositiveSmallIntegerField(default=0)  # 0 = no limit on attempts

    def __str__(self):
        return str(self.name)


def template_file_name(instance, filename):
    return '/'.join(['assignments',
                     str(instance.id),
                     'template',
                     filename
                     ])


def tester_file_name(instance, filename):
    return '/'.join(['assignments',
                     str(instance.id),
                     'tester',
                     filename
                     ])


class CodeFileAssignment(Assignment):
    code_template = models.FileField(upload_to=template_file_name, null=True)
    instructions = models.TextField(blank=True, null=True)
    tester_path = models.FileField(upload_to=tester_file_name)


class QuizAssignment(Assignment):
    questions = models.TextField(blank=True, null=True)  # JSON


class Submission(models.Model):
    points = models.PositiveSmallIntegerField(default=0)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    submitted_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')

    def grade(self):

        # only CodeFileAssignments can be graded via the java grader
        assert hasattr(self.assignment, 'codefileassignment')

        if self.points == 0:  # don't re-grade submissions
            # start grading

            SEPARATOR_SYMBOL = ':' if os.name == 'posix' else ';'
            # posix = *nix (uses : for java separator), nt = windows (uses ;)

            files = self.files.all()

            tmp_build_path = os.path.join(settings.GRADE_TMP_PATH, str(self.id))
            if not os.path.exists(tmp_build_path):
                os.mkdir(tmp_build_path)

            # builds at ./grade_tmp/[submission_id]
            # should be unique enough since submission id is unique
            tester_path = self.assignment.codefileassignment.tester_path.path
            file_paths = [fileField.file.path for fileField in files]
            file_paths.append(tester_path)  # add junit tester to the list of files to be compiled
            # file_paths = ' '.join(file_paths)  # paths separated by spaces
            print(file_paths)
            junit_path = settings.JUNIT_PATH
            json_path = settings.JSON_PATH

            controller = settings.GRADER_CONTROLLER_PATH

            print('starting to compile submission', self.pk)
            # build
            build_cmd = ['javac', '-d', tmp_build_path, '-cp', junit_path]
            build_cmd.extend(file_paths)
            print(build_cmd)
            # build file_paths at tmp_build_path, with a reference to junit in class path
            p = subprocess.Popen(build_cmd,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            output, errors = p.communicate()

            print('compile outputs:')
            print(output)

            print('compile errors:')
            print(errors)

            # track for compilation error
            if errors:
                print(errors.decode())
                message = errors.decode()
                if 'error: invalid flag' in message:
                    message = 'Compilation error: invalid file'
                self.points = 0
                check = SubmissionCheck(name='Compilation', passed=False, details=message,
                                        submission=self)
                check.save()
                self.submitted_date = timezone.now()
                return self.points

            # build controller
            build_controller_cmd = ['javac',
                                    '-d', tmp_build_path,
                                    '-cp', SEPARATOR_SYMBOL.join([tmp_build_path, junit_path, json_path]),
                                    controller]
            print('building controller')
            print(build_controller_cmd)
            # build controller at tmp_build_path, with class paths of the already
            # compiled file_paths files (located at the same tmp_build_path), junit, and json

            p = subprocess.Popen(build_controller_cmd,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            output, errors = p.communicate()

            print('compile outputs:')
            print(output)

            print('compile errors:')
            print(errors)

            # now run the controller to get output from junit test
            cmd = ['java',
                   '-cp', SEPARATOR_SYMBOL.join([tmp_build_path, junit_path, json_path]),
                   'testController']
            print('running assignment code')

            p = subprocess.Popen(cmd,
                                 stdout=subprocess.PIPE)
            output, errors = p.communicate()
            # do something
            print('====== Running Unit Test ======')
            output = json.loads(output.decode())
            print(output)

            # output =
            # {
            #     'points': [earned points],
            #     'total': [total number of tests],
            #     'tests': [{
            #         'name': [name of test],
            #         'passed': [whether the test was successful or not],
            #         'details': [detailed message regarding the failure]
            #     },]
            # }

            self.points = output['points']

            for test in output['tests']:
                check = SubmissionCheck(name=test['name'], passed=test['passed'], details=test['details'], submission=self)
                check.save()

            self.submitted_date = timezone.now()

        return self.points


class SubmissionCheck(models.Model):
    name = models.CharField(max_length=64)
    passed = models.BooleanField()
    details = models.TextField(blank=True, null=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='checks')


def content_file_name(instance, filename):
    now = timezone.now()
    return '/'.join(['uploads',
                     str(instance.submission.student.student_id),
                     str(now.year),
                     str(now.month),
                     str(now.day),
                     str(instance.submission.id),
                     filename
                     ])


class FileUpload(models.Model):
    file = models.FileField(upload_to=content_file_name)
    original_filename = models.CharField(max_length=128)
    upload_date = models.DateTimeField(auto_now_add=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='files')
