# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0002_auto_20170706_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
