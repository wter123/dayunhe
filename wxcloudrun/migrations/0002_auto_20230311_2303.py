# Generated by Django 3.2.8 on 2023-03-11 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxcloudrun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counters',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 23, 3, 31, 5935)),
        ),
        migrations.AlterField(
            model_name='counters',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 23, 3, 31, 5935)),
        ),
    ]
