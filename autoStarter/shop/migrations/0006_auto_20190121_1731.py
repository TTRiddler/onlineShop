# Generated by Django 2.1.5 on 2019-01-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Посчитается после сохранения.', max_digits=10, verbose_name='Цена'),
        ),
    ]