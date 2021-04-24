# Generated by Django 3.2 on 2021-04-12 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_order_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wine_id', models.CharField(max_length=120)),
                ('wine_name', models.CharField(max_length=120)),
                ('qty', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('discount_in_perc', models.CharField(max_length=20)),
                ('case', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.tbl_orders')),
            ],
        ),
    ]