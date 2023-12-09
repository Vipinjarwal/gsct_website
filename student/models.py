from django.db import models

# Create your models here.


class Student(models.Model):
    std_rollno = models.IntegerField(primary_key=True)
    std_name = models.CharField(max_length=255)
    std_father_name = models.CharField(max_length=255)
    std_mother_name = models.CharField(max_length=255)
    std_age = models.DateField()
    std_mobile = models.IntegerField()
    std_address = models.CharField(max_length=500)
    std_course = models.CharField(max_length=255)
    std_image = models.FileField(
        upload_to="profile_images/", max_length=250, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.std_name


class Course(models.Model):
    student = models.OneToOneField(
        Student, verbose_name=("Student"), on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Year(models.Model):
    course = models.OneToOneField(
        Course, verbose_name=("Student"), on_delete=models.CASCADE
    )
    year = models.IntegerField()

    # def __str__(self):
    #     return self.year


class Semester(models.Model):
    year = models.OneToOneField(Year, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Subject(models.Model):
    semester = models.ManyToManyField(Semester)
    subject = models.CharField(max_length=250)

    def __str__(self):
        return self.subject


class Mark(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)


class Result(models.Model):
    marks = models.ForeignKey(Mark, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
