from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FileUpload, Submission
from .serializers import FileUploadSerializer, SubmissionSerializer


class FileUploadViewSet(viewsets.ModelViewSet):

    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer

    parser_classes = (MultiPartParser, FormParser,)  # set parsers if not set in settings. Edited


class SubmissionViewSet(viewsets.ModelViewSet):

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
