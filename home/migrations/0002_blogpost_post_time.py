# Generated by Django 3.2.6 on 2021-08-09 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_time',
            field=models.DateField(default=datetime.datetime(2021, 8, 9, 16, 8, 25, 540415)),
        ),
    ]