# Generated by Django 3.2.5 on 2021-07-06 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locus', '0003_auto_20210706_1433'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Geohash',
            new_name='Geocode',
        ),
        migrations.AlterField(
            model_name='track',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 0, 51, 38, 282834)),
        ),
    ]
