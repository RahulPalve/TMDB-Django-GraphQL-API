# Generated by Django 3.1 on 2020-08-23 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0006_movielist_listtags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielist',
            name='recommended',
        ),
    ]
