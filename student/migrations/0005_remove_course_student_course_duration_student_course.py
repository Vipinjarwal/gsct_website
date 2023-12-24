# Generated by Django 4.2.6 on 2023-12-24 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0004_alter_semester_year"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="student",
        ),
        migrations.AddField(
            model_name="course",
            name="duration",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="course",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="student.course",
                verbose_name="Course",
            ),
            preserve_default=False,
        ),
    ]