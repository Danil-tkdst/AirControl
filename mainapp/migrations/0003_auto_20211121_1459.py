# Generated by Django 3.2.9 on 2021-11-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_unit_commment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='commment',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='aircraft',
            name='type',
            field=models.CharField(max_length=255, null=True, verbose_name='Тип ВС'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Бортовой номер'),
        ),
    ]
