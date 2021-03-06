# Generated by Django 2.1.7 on 2019-02-17 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_auto_20190217_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrelease',
            options={'verbose_name': 'Год выпуска', 'verbose_name_plural': 'Годы выпуска'},
        ),
        migrations.RemoveField(
            model_name='carrelease',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='release_date',
            field=models.ForeignKey(default=2011, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='shop.CarRelease', verbose_name='Год выпуска'),
            preserve_default=False,
        ),
    ]
