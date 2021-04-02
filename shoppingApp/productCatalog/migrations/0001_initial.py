# Generated by Django 3.1.7 on 2021-03-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_serial_num', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('available_quantity', models.IntegerField()),
            ],
        ),
    ]