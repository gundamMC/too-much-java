from django.urls import path, include
from django.views.generic import TemplateView
from .router import router

urlpatterns = [
    path(r'test_page', TemplateView.as_view(template_name="test_page.html"), name="test_page"),
    path(r'api/', include(router.urls)),
    path(r'', TemplateView.as_view(template_name="index.html"), name="app"),
    path(r'<path:resource>', TemplateView.as_view(template_name="index.html"), name="app"),
]
