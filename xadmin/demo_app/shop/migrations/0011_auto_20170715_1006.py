# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-15 02:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_attribute_type_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conment',
            new_name='Comment',
        ),
    ]
