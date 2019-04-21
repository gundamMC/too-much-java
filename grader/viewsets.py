from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import FileUpload, Submission
from .serializers import FileUploadSerializer, SubmissionSerializer


class FileUploadViewSet(viewsets.ModelViewSet):

    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer

    parser_classes = (MultiPartParser, FormParser,)  # set parsers if not set in settings. Edited


class SubmissionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    # def get(self, request, *args, **kwargs):
    #     pass
        # return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def grade(self, request, pk=None):
        print(pk)
        submission = get_object_or_404(Submission, pk=pk)
        grade = submission.grade()
        submission.save()
        return Response({'submissino_id':pk, 'grade': grade})
