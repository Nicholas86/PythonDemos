# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 08:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theuser',
            name='logo',
        ),
    ]
