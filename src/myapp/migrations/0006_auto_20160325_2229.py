# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_ezmap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ezmap',
            name='url',
        ),
        migrations.DeleteModel(
            name='ezMap',
        ),
    ]