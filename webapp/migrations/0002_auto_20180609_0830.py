# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-09 08:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candy',
            name='manufacturedDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 9, 8, 30, 30, 918208, tzinfo=utc), verbose_name='MFD'),
        ),
    ]
