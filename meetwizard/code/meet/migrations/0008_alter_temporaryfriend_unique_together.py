# Generated by Django 3.2.4 on 2021-07-25 01:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meet', '0007_auto_20210724_1151'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='temporaryfriend',
            unique_together={('send_user', 'receive_user')},
        ),
    ]
