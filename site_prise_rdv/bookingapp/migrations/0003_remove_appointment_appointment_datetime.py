# Generated by Django 4.1.6 on 2023-02-09 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0002_appointment_appointment_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_datetime',
        ),
    ]
