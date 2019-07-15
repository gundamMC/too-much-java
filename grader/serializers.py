from datetime import date
import os

from rest_framework import serializers
from .models import FileUpload, Submission, Assignment, CodeFileAssignment, QuizAssignment, Unit, Course, SubmissionCheck

from django.template.defaultfilters import filesizeformat


class FileUploadSerializer(serializers.ModelSerializer):

    original_filename = serializers.ReadOnlyField()

    class Meta:
        model = FileUpload
        fields = '__all__'


class SubmissionCheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubmissionCheck
        fields = ['details', 'name', 'passed']


class SubmissionSerializer(serializers.ModelSerializer):
    files = FileUploadSerializer(many=True, read_only=True)
    checks = SubmissionCheckSerializer(many=True, read_only=True)

    class Meta:
        model = Submission
        fields = '__all__'
        read_only_fields = ('total_points', 'points', 'submitted_date')


class AssignmentSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        if hasattr(instance, 'codefileassignment'):
            print('is code')
            return CodeFileAssignmentSerializer(instance=instance.codefileassignment).data
        else:
            if isinstance(instance, Assignment):
                print('is assignment')
            return BaseAssignmentSerializer(instance=instance).data

    class Meta:
        model = Assignment
        fields = '__all__'


class BaseAssignmentSerializer(serializers.ModelSerializer):

    def get_type(self, obj):
        if hasattr(obj, 'codefileassignment'):
            return 'code'
        elif hasattr(obj, 'quizassignment'):
            return 'quiz'
        else:
            return 'unassigned'

    type = serializers.SerializerMethodField()

    def get_highest_points(self, obj):
        if obj.submissions.count() < 1:
            return -1
        else:
            return obj.submissions.order_by('-points').first().points

    get_highest_points = get_highest_points
    highest_points = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = '__all__'


class CodeFileAssignmentSerializer(BaseAssignmentSerializer):

    def get_file_size(self, obj):
        if obj.code_template is None:
            return None
        return filesizeformat(obj.code_template.size)

    def get_file_name(self, obj):
        if obj.code_template is None:
            return None
        return os.path.basename(obj.code_template.name)

    file_size = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = CodeFileAssignment
        # fields = '__all__'
        exclude = ['tester_path']


class UnitSerializer(serializers.ModelSerializer):

    def get_assignments(self, obj):
        ordered_queryset = obj.assignments.order_by('date')
        return AssignmentSerializer(ordered_queryset, many=True, context=self.context).data

    assignments = serializers.SerializerMethodField()

    def get_latest(self, obj):
        assignments = obj.assignments.filter(due_date__gt=date.today()).order_by('due_date')[:3]
        assignment_ids = [x.id for x in assignments]
        return assignment_ids

    latest = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        # fields = '__all__'
        exclude = ['students']
