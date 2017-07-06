# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail_link', models.CharField(max_length=200)),
                ('img_news', models.ImageField(blank=True, upload_to='news')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
