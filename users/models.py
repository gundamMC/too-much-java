from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.PositiveIntegerField(unique=True)  # maybe even PositiveSmallIntegerField [0, 32767]
    grade = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.student_id)
