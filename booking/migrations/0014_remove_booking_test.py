# Generated by Django 2.0.7 on 2018-08-08 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_booking_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='test',
        ),
    ]