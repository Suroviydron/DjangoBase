# Generated by Django 2.2.13 on 2020-06-08 20:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0005_auto_20200608_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 10, 20, 22, 30, 754437, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]