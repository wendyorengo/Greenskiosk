# Generated by Django 3.1 on 2020-08-20 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_auto_20200820_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coolerbox',
            name='box_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingprovider',
            name='date_joined',
            field=models.DateTimeField(max_length=30),
        ),
    ]