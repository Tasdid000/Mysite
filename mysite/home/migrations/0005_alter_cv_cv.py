# Generated by Django 4.2.1 on 2023-06-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_cv_cv"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cv",
            name="cv",
            field=models.FileField(default="", upload_to="cv/"),
        ),
    ]
