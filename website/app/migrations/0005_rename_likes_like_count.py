# Generated by Django 4.2.1 on 2023-08-27 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_count_like_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='likes',
            new_name='count',
        ),
    ]