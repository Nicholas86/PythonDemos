# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-15 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20170715_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='type_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.Type', verbose_name='\u7c7b\u578b'),
            preserve_default=False,
        ),
    ]
