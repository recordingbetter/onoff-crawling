# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 09:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='slack',
        ),
    ]