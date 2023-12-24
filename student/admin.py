from django.contrib import admin
from .models import Student, Result, Course, Semester, Subject, Year


# Register your models here.
class Resultadmin(admin.ModelAdmin):
    list_display = ["student", "subject", "marks"]


admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Year)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Result, Resultadmin)
