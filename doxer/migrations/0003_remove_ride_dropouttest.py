# Generated by Django 3.2.11 on 2022-11-30 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doxer', '0002_ride_dropouttest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='dropouttest',
        ),
    ]
