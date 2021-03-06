# Generated by Django 2.1.7 on 2019-02-14 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_order_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Delivery', verbose_name='Способ доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Payment', verbose_name='Способ оплаты'),
        ),
    ]
