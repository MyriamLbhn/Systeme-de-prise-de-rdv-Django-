# Generated by Django 4.1.6 on 2023-02-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0009_alter_appointment_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
