# Generated by Django 4.2.20 on 2025-03-24 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mainphoto',
        ),
    ]
