# Generated by Django 3.2.9 on 2021-11-21 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_aircraft_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='garage',
        ),
    ]