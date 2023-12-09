# Generated by Django 4.2.7 on 2023-11-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("std_rollno", models.IntegerField(primary_key=True, serialize=False)),
                ("std_name", models.CharField(max_length=255)),
                ("std_father_name", models.CharField(max_length=255)),
                ("std_mother_name", models.CharField(max_length=255)),
                ("std_age", models.DateField()),
                ("std_mobile", models.IntegerField()),
                ("std_address", models.CharField(max_length=500)),
                ("std_course", models.CharField(max_length=255)),
                (
                    "std_image",
                    models.FileField(
                        blank=True,
                        default=None,
                        max_length=250,
                        null=True,
                        upload_to="profile_images/",
                    ),
                ),
            ],
        ),
    ]
