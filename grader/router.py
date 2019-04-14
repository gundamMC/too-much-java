from rest_framework import routers

from grader.viewsets import FileUploadViewSet, SubmissionViewSet

router = routers.DefaultRouter()
router.register('upload', FileUploadViewSet, base_name='upload')
router.register('submission', SubmissionViewSet, base_name='submission')
