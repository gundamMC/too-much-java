from rest_framework import viewsets
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    http_method_names = ['get']

    def list(self, request, pk=None):
        user = request.user
        student = user.student

        serializer = StudentSerializer(student)

        return Response(serializer.data)
