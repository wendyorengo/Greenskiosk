# Generated by Django 3.1 on 2020-09-08 19:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20200904_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=datetime.datetime(2020, 9, 8, 19, 56, 10, 858259, tzinfo=utc), upload_to='gallery'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='productImage',
        ),
    ]
