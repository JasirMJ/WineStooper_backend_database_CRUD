# Generated by Django 3.2 on 2021-04-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_tbl_order_items_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_orders',
            name='delivery_charge',
            field=models.FloatField(default=20.0),
            preserve_default=False,
        ),
    ]