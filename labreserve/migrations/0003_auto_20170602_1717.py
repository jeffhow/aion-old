# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 17:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labreserve', '0002_auto_20170602_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Reservation Date'),
        ),
    ]
