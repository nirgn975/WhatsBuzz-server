# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whats_buzz', '0010_auto_20160319_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesimagesfb',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whats_buzz.Post'),
        ),
    ]
