# Generated by Django 2.1.5 on 2019-02-08 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0017_auto_20190208_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='call_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 18, 13, 22, 129171), verbose_name='Время звонка'),
        ),
    ]