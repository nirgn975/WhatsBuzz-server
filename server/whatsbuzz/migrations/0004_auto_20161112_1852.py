# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-12 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsbuzz', '0003_auto_20161022_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.TextField(default='12345', max_length=225, verbose_name='user_id'),
            preserve_default=False,
        ),
    ]
