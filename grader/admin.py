from django.contrib import admin

# Register your models here.

from .models import FileUpload, Submission, Assignment, Unit, Course

admin.site.register(Submission)
admin.site.register(FileUpload)
admin.site.register(Assignment)
admin.site.register(Unit)
admin.site.register(Course)
