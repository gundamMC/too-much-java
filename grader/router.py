from rest_framework import routers

from grader.viewsets import FileUploadViewSet, SubmissionViewSet, CourseViewSet, AssignmentViewSet
from users.viewsets import StudentViewSet, RegisterViewSet

router = routers.DefaultRouter()
router.register('upload', FileUploadViewSet, base_name='upload')
router.register('submission', SubmissionViewSet, base_name='submission')
router.register('assignment', AssignmentViewSet, base_name='assignment')
# router.register('unit', UnitViewSet, base_name='unit')
router.register('course', CourseViewSet, base_name='course')
router.register('user', StudentViewSet, base_name='user')
router.register('register', RegisterViewSet, base_name='register')
