# Generated by Django 2.1.5 on 2019-02-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20190210_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cars',
            field=models.ManyToManyField(blank=True, null=True, to='shop.Car', verbose_name='Автомобили'),
        ),
    ]