from django.contrib import admin

# Register your models here.

from .models import FileUpload, Submission, Assignment, CodeFileAssignment, QuizAssignment, Unit, Course, CourseCode

admin.site.register(Submission)
admin.site.register(FileUpload)
admin.site.register(Assignment)
admin.site.register(CodeFileAssignment)
admin.site.register(QuizAssignment)
admin.site.register(Unit)
admin.site.register(Course)
admin.site.register(CourseCode)
