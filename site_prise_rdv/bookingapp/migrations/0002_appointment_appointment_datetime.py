# Generated by Django 4.1.6 on 2023-02-09 00:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]