from rest_framework import serializers
from .models import FileUpload, Submission, Assignment, Unit, Course


class FileUploadSerializer(serializers.ModelSerializer):

    original_filename = serializers.ReadOnlyField()

    class Meta:
        model = FileUpload
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    assignments = AssignmentSerializer(many=True, read_only=True)

    class Meta:
        model = Unit
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
