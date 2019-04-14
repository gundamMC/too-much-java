from rest_framework import serializers
from .models import FileUpload, Submission


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileUpload
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = '__all__'
