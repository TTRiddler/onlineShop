# Generated by Django 2.1.5 on 2019-01-21 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190121_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
