# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-12 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=360, verbose_name='\u540d\u79f0')),
                ('content', models.CharField(max_length=360, verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
    ]
