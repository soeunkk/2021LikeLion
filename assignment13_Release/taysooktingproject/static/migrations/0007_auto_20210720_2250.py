# Generated by Django 3.2 on 2021-07-20 13:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crudapp', '0006_auto_20210720_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='users_like',
            field=models.ManyToManyField(related_name='user_like', through='crudapp.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='users_scrap',
            field=models.ManyToManyField(related_name='user_scrap', through='crudapp.Scrap', to=settings.AUTH_USER_MODEL),
        ),
    ]
