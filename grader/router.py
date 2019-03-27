from rest_framework import routers

from grader.viewsets import FileUploadViewSet

router = routers.DefaultRouter()
router.register('upload', FileUploadViewSet, base_name='upload')
