# Generated by Django 2.1.5 on 2019-02-08 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0016_auto_20190208_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='call_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 18, 12, 33, 805295), verbose_name='Время звонка'),
        ),
    ]