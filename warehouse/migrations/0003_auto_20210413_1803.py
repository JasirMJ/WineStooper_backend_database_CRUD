# Generated by Django 3.2 on 2021-04-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_tbl_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_wines',
            name='bottle_cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tbl_wines',
            name='case_cost',
            field=models.FloatField(),
        ),
    ]
