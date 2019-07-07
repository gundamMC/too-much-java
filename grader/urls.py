from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .router import router
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path(r'api/auth/obtain_token/', obtain_jwt_token),
    path(r'api/auth/refresh_token/', refresh_jwt_token),
    path(r'api/', include(router.urls)),
    path(r'', TemplateView.as_view(template_name="index.html"), name="app"),
    # path(r'<path:resource>', TemplateView.as_view(template_name="index.html"), name="app"),
    re_path(r'^(?P<path>.*)/$', TemplateView.as_view(template_name="index.html")),
]
