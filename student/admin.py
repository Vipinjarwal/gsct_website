from django.contrib import admin
from .models import Student, Result, Course, Semester, Subject

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "std_rollno",
        "std_name",
        "std_mobile",
        "std_course",
    ]


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class ResultAdmin(admin.ModelAdmin):
    list_display = ["student", "course"]


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Semester)
admin.site.register(Subject)
# admin.site.register(Mark)
admin.site.register(Result)
