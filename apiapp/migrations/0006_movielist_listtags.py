# Generated by Django 3.1 on 2020-08-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0005_movie_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='listtags',
            field=models.TextField(null=True),
        ),
    ]