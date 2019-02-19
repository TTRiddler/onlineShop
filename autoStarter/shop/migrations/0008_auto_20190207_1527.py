# Generated by Django 2.1.5 on 2019-02-07 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190207_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Модель авто')),
                ('release_date', models.DateField(verbose_name='Год выпуска')),
            ],
            options={
                'verbose_name': 'Модель авто',
                'verbose_name_plural': 'Модели авто',
            },
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Марка авто')),
            ],
            options={
                'verbose_name': 'Марка авто',
                'verbose_name_plural': 'Марки авто',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='shop.CarBrand', verbose_name='Марка авто'),
        ),
        migrations.AddField(
            model_name='product',
            name='nanufacturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Manufacturer', verbose_name='Производитель'),
            preserve_default=False,
        ),
    ]