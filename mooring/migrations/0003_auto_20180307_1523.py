# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-07 07:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0002_auto_20180227_1115'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marina',
            new_name='MarinePark',
        ),
    ]
