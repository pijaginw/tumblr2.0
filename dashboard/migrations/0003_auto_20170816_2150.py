# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_note_note_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_type',
            field=models.CharField(default='R', max_length=2),
        ),
    ]
