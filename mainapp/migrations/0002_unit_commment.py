# Generated by Django 3.2.9 on 2021-11-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='commment',
            field=models.CharField(max_length=1000, null=True, verbose_name='Комментарий'),
        ),
    ]
