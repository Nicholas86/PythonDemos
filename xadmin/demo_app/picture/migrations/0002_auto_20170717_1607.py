# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodspicture',
            name='adversitation_position',
            field=models.CharField(choices=[('0', '\u56de\u8d2d\u533a\u8f6e\u64ad\u56fe'), ('1', '\u9996\u9875\u63a8\u83503'), ('2', '\u9996\u9875\u63a8\u83502'), ('3', '\u9996\u9875\u63a8\u83501'), ('4', '\u9996\u9875\u8f6e\u64ad\u56fe')], max_length=255, verbose_name='\u8f6e\u64ad\u56fe\u4f4d\u7f6e'),
        ),
        migrations.AlterField(
            model_name='goodspicture',
            name='is_show',
            field=models.CharField(choices=[('1', '\u662f'), ('0', '\u5426')], max_length=255, verbose_name='\u662f\u5426\u663e\u793a'),
        ),
    ]
