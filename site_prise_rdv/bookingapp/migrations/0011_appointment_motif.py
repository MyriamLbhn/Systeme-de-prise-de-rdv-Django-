# Generated by Django 4.1.6 on 2023-02-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0010_alter_appointment_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='motif',
            field=models.TextField(blank=True),
        ),
    ]
