import subprocess
import os
import json
import datetime

from shutil import copy

from django.db import models

from users.models import Student

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return str(self.name)


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


def starting_file_name(instance, filename):
    return '/'.join(['assignment_templates',
                     str(instance.id),
                     filename
                     ])


class CodeFileAssignment(Assignment):
    code_template = models.FileField(upload_to=starting_file_name, null=True)
    instructions = models.TextField(blank=True, null=True)
    public_test_cases = models.TextField(blank=True, null=True)  # JSON list since we can't store lists directly
    private_test_cases = models.TextField(blank=True, null=True)  # JSON


class QuizAssignment(Assignment):
    questions = models.TextField(blank=True, null=True)  # JSON


class Submission(models.Model):
    points = models.PositiveSmallIntegerField(default=0)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    submitted_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')

    def grade(self):
        if self.points is None:
            files = self.files.all()

            tmp_path = r'D:\tmp'
            junit_path = r'D:\junit-platform-console-standalone-1.4.2.jar'
            json_path = r'D:\json-20180813.jar'

            package_path = os.path.join(tmp_path, 'tester')
            build_path = os.path.join(tmp_path, 'build')

            file_paths = []
            for fileField in files:
                print(fileField.file.path)
                url = copy(fileField.file.path, package_path)
                file_paths.append(url)
                print(url)

            controller = r'D:\testController.java'

            # build
            build_cmd = r'javac -d {0} -cp {1} {2}'.format(build_path, junit_path, ' '.join(file_paths))
            p = subprocess.Popen(build_cmd,
                                 stdout=subprocess.PIPE)
            output, errors = p.communicate()
            print('====== Compiling ======')
            print(output.decode())

            # precompile controller?
            build_controller_cmd = r'javac -d {0} -cp {1};{2};{3} {4}'.format(build_path, build_path, junit_path, json_path, controller)
            p = subprocess.Popen(build_controller_cmd,
                                 stdout=subprocess.PIPE)
            output, errors = p.communicate()
            print('====== Compiling Controller ======')
            print(output.decode())

            cmd = r'java -cp {0};{1};{2} testController'.format(build_path, junit_path, json_path)

            p = subprocess.Popen(cmd,
                                 stdout=subprocess.PIPE)
            output, errors = p.communicate()
            # do something
            print('====== Running Unit Test ======')
            output = json.loads(output.decode())
            print(output)

            # self.points = output['points']
            # self.total_points = output['total']
            self.submitted_date = datetime.datetime.now()

        return self.points


def content_file_name(instance, filename):
    now = datetime.datetime.now()
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
