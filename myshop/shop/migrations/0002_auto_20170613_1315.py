# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 05:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': '\u5546\u54c1\u5206\u7c7b', 'verbose_name_plural': '\u5546\u54c1\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': '\u5546\u54c1\u540d\u79f0', 'verbose_name_plural': '\u5546\u54c1\u540d\u79f0'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='update',
            new_name='updated',
        ),
    ]
