# Generated by Django 2.1.5 on 2019-02-07 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0005_auto_20190207_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='call_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 15, 0, 45, 950005), verbose_name='Время звонка'),
        ),
    ]