# Generated by Django 2.2.7 on 2019-11-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.png', upload_to='user_images'),
        ),
    ]
