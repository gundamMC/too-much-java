from rest_framework import serializers
from .models import FileUpload, Submission, Assignment, CodeFileAssignment, QuizAssignment, Unit, Course


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

    def get_type(self, obj):
        if hasattr(obj, 'codefileassignment'):
            return 'code'
        elif hasattr(obj, 'quizassignment'):
            return 'quiz'
        else:
            return 'unassigned'

    type = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):

    def get_assignments(self, obj):
        ordered_queryset = obj.assignments.order_by('date')
        return AssignmentSerializer(ordered_queryset, many=True, context=self.context).data

    assignments = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
