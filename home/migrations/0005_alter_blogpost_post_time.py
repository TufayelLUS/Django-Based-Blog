# Generated by Django 3.2.6 on 2021-08-12 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210811_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]