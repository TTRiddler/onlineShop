# Generated by Django 2.1.5 on 2019-01-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
    ]
