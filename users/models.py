from django.contrib.auth.models import User
from django.db import models

from grader.models import Class


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.PositiveIntegerField()  # maybe even PositiveSmallIntegerField [0, 32767]
    grade = models.PositiveSmallIntegerField()

    classes = models.ManyToManyField(Class)
