# models.py

from django.db import models
from django.core.validators import MaxValueValidator


class Student(models.Model):
    roll_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    # Add any other fields you need for the student

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.roll_number}"


class Result(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    marks_math = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MaxValueValidator(100)]
    )
    marks_science = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MaxValueValidator(100)]
    )
    marks_history = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MaxValueValidator(100)],
        verbose_name="Marks History",
    )
    max_marks = models.PositiveIntegerField(
        default=100, validators=[MaxValueValidator(100)]
    )
    result_date = models.DateField()
    result_semester = models.IntegerField()

    # Add any other fields you need for the result

    def __str__(self):
        return f"Result for {self.student.first_name} {self.student.last_name} - {self.student.roll_number} on {self.result_date}"
