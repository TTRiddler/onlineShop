# Generated by Django 2.1.5 on 2019-02-08 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0031_auto_20190208_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='call_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 19, 28, 19, 89261), verbose_name='Время звонка'),
        ),
    ]