# Generated by Django 3.1 on 2020-08-20 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAddres',
            new_name='ShippingAddress',
        ),
    ]
