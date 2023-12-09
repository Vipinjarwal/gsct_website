# Generated by Django 4.2.7 on 2023-12-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0008_mark_alter_result_semster_alter_result_subject_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mark",
            name="name",
        ),
        migrations.RemoveField(
            model_name="result",
            name="marks",
        ),
        migrations.AddField(
            model_name="mark",
            name="marks",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="result",
            name="grade",
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]