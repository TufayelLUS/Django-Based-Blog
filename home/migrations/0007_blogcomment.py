# Generated by Django 3.2.6 on 2021-08-17 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_blogpost_blog_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_slug', models.CharField(default='', max_length=100)),
                ('comment_owner', models.CharField(max_length=100)),
                ('comment_text', models.TextField(max_length=1024280)),
                ('comment_time', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
