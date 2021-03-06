# Generated by Django 3.2.12 on 2022-02-12 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='avtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
