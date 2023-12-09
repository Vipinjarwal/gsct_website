# Generated by Django 4.2.7 on 2023-12-05 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0014_remove_result_course_remove_result_semster_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="semester",
            name="year",
        ),
        migrations.AddField(
            model_name="semester",
            name="course",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="student.course",
                verbose_name="Student",
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Year",
        ),
    ]
