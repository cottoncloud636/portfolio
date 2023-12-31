# Generated by Django 4.2.1 on 2023-08-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='static/assets/media/')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
