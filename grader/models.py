from django.db import models

# Create your models here.


class Submission(models.Model):
    total_points = models.IntegerField()
    points = models.IntegerField()

    def grade(self):
        # do something
        self.points = 5


class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

