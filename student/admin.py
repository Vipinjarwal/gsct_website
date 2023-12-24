from django.contrib import admin
from .models import Student, Result, Course, Semester, Subject, Year

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "std_rollno",
        "std_name",
        "std_mobile",
    ]


admin.site.register(Course)
admin.site.register(Student, StudentAdmin)
admin.site.register(Year)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Result)
