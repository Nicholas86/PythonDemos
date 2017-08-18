# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170717_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consignee_address', models.CharField(max_length=5555, verbose_name='\u6536\u8d27\u4eba\u5730\u5740')),
                ('consignee_telphone', models.CharField(max_length=255, verbose_name='\u624b\u673a\u53f7')),
                ('consignee_name', models.CharField(max_length=255, verbose_name='\u6536\u8d27\u4eba\u59d3\u540d')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.TheUser', verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u5730\u5740\u7ba1\u7406',
                'verbose_name_plural': '\u5730\u5740\u7ba1\u7406',
            },
        ),
    ]
