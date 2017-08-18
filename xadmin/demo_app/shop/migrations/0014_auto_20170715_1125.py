# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-15 03:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='goods_id',
        ),
        migrations.AlterModelOptions(
            name='attribute',
            options={'verbose_name': '\u5c5e\u6027\u7ba1\u7406', 'verbose_name_plural': '\u5c5e\u6027\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': '\u54c1\u724c\u7ba1\u7406', 'verbose_name_plural': '\u54c1\u724c\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u5206\u7c7b\u7ba1\u7406', 'verbose_name_plural': '\u5206\u7c7b\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '\u5546\u54c1\u7ba1\u7406', 'verbose_name_plural': '\u5546\u54c1\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': '\u7c7b\u578b\u7ba1\u7406', 'verbose_name_plural': '\u7c7b\u578b\u7ba1\u7406'},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
