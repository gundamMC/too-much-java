from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

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
        user = UserModel.objects.create(
            username=validated_data['username_reg']
        )
        user.set_password(validated_data['password'])
        user.save()

        student = Student.objects.create(
            user=user,
            student_id=validated_data['student_id'],
            grade=validated_data['grade']
        )
        student.save()

        return student

    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }
