from datetime import date

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, generics, status
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
        serializer.save(original_filename=str(self.request.FILES['file']))


class SubmissionViewSet(viewsets.ModelViewSet):

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        submission = serializer.save()
        submission.total_points = submission.assignment.points
        submission.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['post'], detail=False)
    def test(self, request):

        print('test')
        print(request.data)

        return Response()

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

    @action(methods=['get'], detail=True)
    def latest(self, request, pk=None):
        unit = get_object_or_404(Unit, pk=pk)
        assignments = unit.assignments.filter(due_date__gt=date.today()).order_by('due_date')[:3]
        return Response({
            'unit_id': pk,
            'assignments': AssignmentSerializer(assignments, many=True).data
        })


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
