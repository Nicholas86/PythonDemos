# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-13 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import shop.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170713_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('parent_id', models.IntegerField(verbose_name='\u7236\u7ea7id')),
                ('addtime', models.DateTimeField(auto_now_add=True, max_length=255, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('order', shop.fields.OrderField(blank=True)),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
    ]