# Generated by Django 4.2.1 on 2023-06-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="cv",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("cv", models.FileField(upload_to="static/cv/")),
            ],
        ),
    ]
