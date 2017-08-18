# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_address_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.TheUser', verbose_name='\u7528\u6237'),
            preserve_default=False,
        ),
    ]