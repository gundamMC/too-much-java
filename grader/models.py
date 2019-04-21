import subprocess

from django.db import models

# Create your models here.


class Submission(models.Model):
    total_points = models.IntegerField()
    points = models.IntegerField(default=None, blank=True, null=True)

    def grade(self):

        if self.points is None:
            test_path = r'java -cp D:\autograder\src\build\out;D:\autograder\src\build\out\junit-platform-console-standalone-1.4.2.jar tester.testController'
            p = subprocess.Popen(test_path,
                                 stdout=subprocess.PIPE)
            output, errors = p.communicate()
            # do something
            print(output.decode())
            self.points = 5
        return self.points


class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

