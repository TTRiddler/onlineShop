# Generated by Django 2.1.5 on 2019-02-07 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0009_auto_20190207_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='call_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 16, 1, 4, 137529), verbose_name='Время звонка'),
        ),
    ]
