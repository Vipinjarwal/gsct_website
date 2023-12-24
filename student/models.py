from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=250)
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class Year(models.Model):
    course = models.OneToOneField(
        Course, verbose_name=("Student"), on_delete=models.CASCADE
    )
    year = models.IntegerField()

    def __str__(self):
        return f"{self.year} : {self.course}"


class Semester(models.Model):
    year = models.ForeignKey(Year, verbose_name=("Year"), on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.year} : {self.name}"


class Student(models.Model):
    course = models.ForeignKey(
        Course, verbose_name=("Course"), on_delete=models.CASCADE
    )
    year = models.ForeignKey(Year, verbose_name=("Year"), on_delete=models.CASCADE)
    semester = models.ForeignKey(
        Semester, verbose_name=("Semester"), on_delete=models.CASCADE
    )
    std_rollno = models.IntegerField(primary_key=True)
    std_name = models.CharField(max_length=255)
    std_father_name = models.CharField(max_length=255)
    std_mother_name = models.CharField(max_length=255)
    std_age = models.DateField()
    std_mobile = models.IntegerField()
    std_address = models.CharField(max_length=500)
    std_image = models.FileField(
        upload_to="profile_images/", max_length=250, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.std_name


class Subject(models.Model):
    semester = models.ForeignKey(
        Semester, verbose_name=("Semester"), on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.semester} : {self.subject}"


class Result(models.Model):
    student = models.ForeignKey(
        Student, verbose_name=("Student"), on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject, verbose_name=("Subject"), on_delete=models.CASCADE
    )
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student} : {self.subject} - {self.marks}"
