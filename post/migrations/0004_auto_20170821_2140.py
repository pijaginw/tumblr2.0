# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170816_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.Note')),
            ],
            bases=('post.note',),
        ),
        migrations.CreateModel(
            name='Reblog',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.Note')),
            ],
            bases=('post.note',),
        ),
        migrations.RemoveField(
            model_name='note',
            name='note_text',
        ),
        migrations.RemoveField(
            model_name='note',
            name='note_type',
        ),
        migrations.RemoveField(
            model_name='note',
            name='reblogs',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='post_value',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AddField(
            model_name='post',
            name='reblogs',
            field=models.IntegerField(default=0),
        ),
    ]
