# Generated by Django 3.2.9 on 2021-12-10 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20211130_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='aircraft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unt', to='mainapp.aircraft', verbose_name='ВС'),
        ),
    ]
