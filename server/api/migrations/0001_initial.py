# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 08:13
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookGamesImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(blank=True, upload_to='posts/%Y/%m/%d/', verbose_name='background image')),
            ],
            options={
                'verbose_name': 'facebook background image',
                'verbose_name_plural': 'facebook background images',
            },
        ),
        migrations.CreateModel(
            name='FacebookProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveIntegerField(verbose_name='width')),
                ('height', models.PositiveIntegerField(verbose_name='height')),
                ('x', models.PositiveIntegerField(verbose_name='x')),
                ('y', models.PositiveIntegerField(verbose_name='y')),
            ],
            options={
                'verbose_name': 'facebook profile image',
                'verbose_name_plural': 'facebook profile images',
            },
        ),
        migrations.CreateModel(
            name='FacebookUsername',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(choices=[('empty', ''), ('first_name', 'First Name'), ('last_name', 'Last Name'), ('full_name', 'First and Last Name')], default='empty', max_length=255, verbose_name='username')),
                ('x', models.PositiveIntegerField(verbose_name='x')),
                ('y', models.PositiveIntegerField(verbose_name='y')),
                ('color', models.CharField(max_length=255, verbose_name='color')),
                ('font_size', models.PositiveIntegerField(verbose_name='font_size')),
                ('text_align', models.CharField(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], default='center', max_length=225, verbose_name='text align')),
            ],
            options={
                'verbose_name': 'facebook username',
                'verbose_name_plural': 'facebook usernames',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='title')),
                ('title_he', models.CharField(blank=True, max_length=255, null=True, verbose_name='title')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='title')),
                ('body', ckeditor.fields.RichTextField(blank=True, verbose_name='body')),
                ('body_he', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='body')),
                ('body_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='body')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('banner_image', models.ImageField(blank=True, upload_to='posts/%Y/%m/%d/', verbose_name='banner image')),
                ('buzz', models.BooleanField(default=False, verbose_name='buzz')),
                ('age_categories', models.CharField(choices=[('default', 'Default'), ('children', 'Children'), ('young', 'Young'), ('adults', 'Adults')], default='default', max_length=25, verbose_name='age categories')),
                ('publish', models.DateTimeField(null=True, verbose_name='publish')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='tag')),
                ('name_he', models.CharField(max_length=255, null=True, verbose_name='tag')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('user_id', models.TextField(max_length=225, verbose_name='user_id')),
                ('name', models.CharField(max_length=225, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_time_visit', models.DateTimeField(verbose_name='last_time_visit')),
            ],
            options={
                'verbose_name': 'Facebook User',
                'verbose_name_plural': 'Facebook Users',
            },
        ),
        migrations.CreateModel(
            name='FacebookGame',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Post')),
            ],
            options={
                'verbose_name': 'Facebook Game',
                'verbose_name_plural': 'Facebook Games',
            },
            bases=('api.post',),
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Post')),
                ('code', models.TextField(verbose_name='code')),
                ('code_he', models.TextField(null=True, verbose_name='code')),
                ('code_en', models.TextField(null=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Trend',
                'verbose_name_plural': 'Trends',
            },
            bases=('api.post',),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='api.Tags'),
        ),
        migrations.AddField(
            model_name='facebookusername',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facebook_username', to='api.FacebookGame'),
        ),
        migrations.AddField(
            model_name='facebookprofileimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facebook_profile_image', to='api.FacebookGame'),
        ),
        migrations.AddField(
            model_name='facebookgamesimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='background_image', to='api.FacebookGame'),
        ),
    ]
