# Generated by Django 2.1.5 on 2019-02-07 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0008_auto_20190207_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='call_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 16, 0, 15, 552936), verbose_name='Время звонка'),
        ),
    ]