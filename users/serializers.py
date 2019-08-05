from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from grader.models import CourseCode
from .models import Student


UserModel = get_user_model()


class StudentSerializer(serializers.ModelSerializer):

    def get_username(self, obj):
        return obj.user.username

    username = SerializerMethodField()

    username_reg = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    code = serializers.CharField(write_only=True)

    def create(self, validated_data):
        code = validated_data['code']
        try:
            course_code_object = CourseCode.objects.get(code=code)
        except CourseCode.DoesNotExist:
            raise serializers.ValidationError("Invalid course code")

        try:
            user = UserModel.objects.create(
                username=validated_data['username_reg']
            )
            user.set_password(validated_data['password'])
            user.save()
        except IntegrityError:
            raise serializers.ValidationError("Username already used")

        try:
            student = Student.objects.create(
                user=user,
                student_id=validated_data['student_id'],
                grade=validated_data['grade'],
            )

            student.courses.set(course_code_object.courses.all())
            # automatically enroll the student to the course

            student.save()
        except IntegrityError:
            user.delete()
            raise serializers.ValidationError("Student ID already used")

        return student

    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }
