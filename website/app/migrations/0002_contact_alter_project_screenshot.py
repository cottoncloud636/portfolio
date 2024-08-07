# Generated by Django 4.2.1 on 2023-08-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=15)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='static/assets/media/'),
        ),
    ]
