# Generated by Django 5.1 on 2024-09-09 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(upload_to='doctors/doctors/'),
        ),
    ]
