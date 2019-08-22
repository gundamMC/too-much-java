from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import FileUpload, Submission, Assignment, Unit, Course
from .serializers import FileUploadSerializer, SubmissionSerializer, AssignmentSerializer, UnitSerializer, CourseSerializer


class FileUploadViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer

    parser_classes = (MultiPartParser, FormParser,)

    # disabling get file upload directly
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(original_filename=str(self.request.FILES['file']))


class SubmissionViewSet(viewsets.ModelViewSet):

    # queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    # set query set to the student's own submissions only
    def get_queryset(self):
        return self.request.user.student.submissions.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        data['student'] = request.user.student.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        submission = serializer.save()
        submission.total_points = submission.assignment.points
        # submission.grade()
        submission.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['get'], detail=True)
    def grade(self, request, pk=None):
        submission = get_object_or_404(Submission, pk=pk)
        submission.grade()
        submission.save()
        return Response(SubmissionSerializer(
            submission.assignment.submissions.filter(student=request.user.student.id), many=True).data)

    # @action(methods=['get'], detail=True)
    # def files(self, request, pk=None):
    #     submission = get_object_or_404(Submission, pk=pk)
    #     return Response({
    #         'submission_id': pk,
    #         'files': FileUploadSerializer(submission.files.all(), many=True).data
    #         })


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    @action(methods=['get'], detail=True)
    def submissions(self, request, pk=None):
        assignment = get_object_or_404(Assignment, pk=pk)
        results = assignment.submissions.filter(student__student_id=request.user.student.student_id)
        return Response(SubmissionSerializer(results, many=True).data)


#
# class UnitViewSet(viewsets.ModelViewSet):
#     queryset = Unit.objects.all()
#     serializer_class = UnitSerializer


class CourseViewSet(viewsets.ModelViewSet):
    # queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        return self.request.user.student.courses.all()
