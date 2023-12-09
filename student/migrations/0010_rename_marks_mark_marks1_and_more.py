# Generated by Django 4.2.7 on 2023-12-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0009_remove_mark_name_remove_result_marks_mark_marks_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mark",
            old_name="marks",
            new_name="marks1",
        ),
        migrations.RenameField(
            model_name="subject",
            old_name="name",
            new_name="subject1",
        ),
        migrations.AddField(
            model_name="mark",
            name="marks2",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mark",
            name="marks3",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mark",
            name="marks4",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="subject2",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="subject3",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="subject4",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]