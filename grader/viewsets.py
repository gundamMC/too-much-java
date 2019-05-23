from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import FileUpload, Submission, Assignment, Unit, Course
from .serializers import FileUploadSerializer, SubmissionSerializer, AssignmentSerializer, UnitSerializer, CourseSerializer


class FileUploadViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer

    parser_classes = (MultiPartParser, FormParser,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(original_filename = str(self.request.FILES['file']))


class SubmissionViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def grade(self, request, pk=None):
        print(pk)
        submission = get_object_or_404(Submission, pk=pk)
        grade = submission.grade()
        submission.save()
        return Response({'submission_id': pk, 'grade': grade})

    @action(methods=['get'], detail=True)
    def files(self, request, pk=None):
        submission = get_object_or_404(Submission, pk=pk)
        return Response({
            'submission_id': pk,
            'files': FileUploadSerializer(submission.fileupload_set.all(), many=True).data
            })


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
