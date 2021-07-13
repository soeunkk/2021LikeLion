# Generated by Django 3.2.4 on 2021-07-01 16:13

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(max_length=200)),
                ('food', models.CharField(max_length=200)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('review', models.TextField(null=True)),
                ('food_image', models.ImageField(null=True, upload_to='images/')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='data published')),
            ],
        ),
    ]
