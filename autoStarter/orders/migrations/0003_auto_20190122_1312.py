# Generated by Django 2.1.5 on 2019-01-22 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190122_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='fio',
            new_name='full_name',
        ),
    ]