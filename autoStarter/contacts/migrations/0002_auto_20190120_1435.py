# Generated by Django 2.1.5 on 2019-01-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='name',
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Адрес'),
        ),
    ]