# Generated by Django 5.1 on 2024-09-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_doctor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(upload_to='doctors/'),
        ),
    ]
