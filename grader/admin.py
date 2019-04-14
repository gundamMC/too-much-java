from django.contrib import admin

# Register your models here.

from .models import FileUpload, Submission

admin.site.register(Submission)
admin.site.register(FileUpload)
