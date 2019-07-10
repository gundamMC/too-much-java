from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ViewSet):
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer

    http_method_names = ['get']

    # set query set to the student's own submissions only
    def list(self, request):
        serializer = StudentSerializer(request.user.student, many=False)
        return Response(serializer.data)


class RegisterViewSet(CreateModelMixin, GenericViewSet):

    model = Student
    permission_classes = [
        permissions.AllowAny  # Or new users can't register
    ]
    serializer_class = StudentSerializer
