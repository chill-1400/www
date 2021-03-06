# Generated by Django 3.2.12 on 2022-02-19 22:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220213_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(default='', max_length=100, verbose_name='E-mail отправителя')),
                ('subject', models.CharField(max_length=100, verbose_name='Тема сообщения')),
                ('text', models.TextField(verbose_name='Письмо')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата отправки')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
    ]
