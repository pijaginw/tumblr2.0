# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170816_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='post',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
