# Generated by Django 3.2.19 on 2023-08-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('certificate', models.ImageField(default='', upload_to='certificate')),
            ],
        ),
    ]