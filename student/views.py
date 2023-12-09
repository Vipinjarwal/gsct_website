from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Course
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.
def home(request):
    return render(request, "index.html")


def courses(request):
    return render(request, "courses.html")


def courseshow(request):
    courses = Course.objects.all().values()

    return render(request, "courseshow.html", {"courses": courses})


def coursedetails(request, id):
    course = Course.objects.get(pk=id)
    print(course)

    return render(request, "coursedetails.html", {"course": course})


def studenthub(request):
    if request.method == "POST":
        std_roll = request.POST.get("rollno")
        std_age = request.POST.get("age")
        print(std_roll, std_age)

        std = Student.objects.filter(std_rollno=std_roll, std_age=std_age).values()
        print(std)

        if std:
            return render(request, "studentpannel.html", {"std": std})

        else:
            messages.error(request, "Student Not Found")
            return redirect("/studenthub/")

    return render(request, "studentinfo.html")


def aboutus(request):
    return render(request, "about.html")


def contactus(request):
    return render(request, "contact.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invailid username")
            return redirect("/login/")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invaild Password")
            return redirect("/login/")

        else:
            login(request, user)
            return redirect("/admin/")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/login/")


@login_required(login_url="/login/")
def student_create_show(request):
    if request.method == "POST":
        std_rollno = request.POST.get("std_rollno")
        std_name = request.POST.get("std_name").upper()
        std_father_name = request.POST.get("std_father_name").upper()
        std_mother_name = request.POST.get("std_mother_name").upper()
        std_age = request.POST.get("std_age")
        std_mobile = request.POST.get("std_mobile")
        std_address = request.POST.get("std_address").upper()
        std_course = request.POST.get("std_course").upper()
        std_image = request.FILES.get("std_image")

        if Student.objects.filter(std_rollno=std_rollno):
            messages.error(request, "Student rollno already exists")
            return redirect("/admin/")

        else:
            Student.objects.create(
                std_rollno=std_rollno,
                std_name=std_name,
                std_father_name=std_father_name,
                std_mother_name=std_mother_name,
                std_age=std_age,
                std_mobile=std_mobile,
                std_address=std_address,
                std_course=std_course,
                std_image=std_image,
            )
            messages.success(request, "Student Created Successfully")
            return redirect("/admin/")

    else:
        std = Student.objects.all()

        search_q = request.GET.get("search")
        if search_q:
            queryset = std.filter(std_name__icontains=search_q)
            context = {"std": queryset}
            return render(request, "admin.html", context)
        return render(request, "admin.html", {"std": std})


def student_data(request, id):
    std = Student.objects.get(pk=id)
    return render(request, "profile.html", {"std": std})


def student_update(request, id):
    std = Student.objects.get(pk=id)
    return render(request, "student_update.html", {"std": std})


def student_doupdate(request, id):
    if request.method == "POST":
        std_rollno = request.POST.get("std_rollno")
        std_name = request.POST.get("std_name").upper()
        std_father_name = request.POST.get("std_father_name").upper()
        std_mother_name = request.POST.get("std_mother_name").upper()
        std_mobile = request.POST.get("std_mobile")
        std_address = request.POST.get("std_address").upper()
        std_course = request.POST.get("std_course").upper()
        std_image = request.FILES.get("std_image")
        std_age = request.POST.get("std_age")

        std = Student.objects.get(pk=id)

        std.std_rollno = std_rollno
        std.std_name = std_name
        std.std_father_name = std_father_name
        std.std_mother_name = std_mother_name
        std.std_mobile = std_mobile
        std.std_address = std_address
        std.std_course = std_course
        if std_image:
            std.std_image = std_image
            std.save()
        elif std_age:
            std.std_age = std_age
            std.save()
        std.save()
        return redirect("/admin/")


def student_delete(request, id):
    std = Student.objects.get(pk=id)
    std.delete()
    return redirect("/admin/")
