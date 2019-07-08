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

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    # set query set to the student's own submissions only
    def get_queryset(self):
        return self.request.user.student.submissions.all()

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
            'files': FileUploadSerializer(submission.files.all(), many=True).data
            })


# Not needed since everything can be obtained from the course api
#
# class AssignmentViewSet(viewsets.ModelViewSet):
#     queryset = Assignment.objects.all()
#     serializer_class = AssignmentSerializer
#
#
# class UnitViewSet(viewsets.ModelViewSet):
#     queryset = Unit.objects.all()
#     serializer_class = UnitSerializer


class CourseViewSet(viewsets.ModelViewSet):
    # queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        return self.request.user.student.courses.all()
