# Generated by Django 3.2.5 on 2021-07-06 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geohash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_code', models.CharField(default='', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('expiry_time', models.DateTimeField(default=datetime.datetime(2021, 7, 7, 0, 25, 5, 57603))),
                ('track_title', models.CharField(default='', max_length=100)),
                ('track_author', models.CharField(default='', max_length=100)),
                ('track_url', models.URLField(default='')),
            ],
            options={
                'ordering': ('time_added',),
            },
        ),
    ]
