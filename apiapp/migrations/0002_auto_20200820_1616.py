# Generated by Django 3.1 on 2020-08-20 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='video_average',
            new_name='vote_average',
        ),
    ]