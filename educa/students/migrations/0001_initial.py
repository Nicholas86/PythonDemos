# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courese', '0004_auto_20170620_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200, verbose_name='\u8bfe\u7a0b\u540d\u79f0')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courese.Course')),
            ],
            options={
                'verbose_name': '\u62a5\u540d\u7684\u8bfe\u7a0b',
                'verbose_name_plural': '\u62a5\u540d\u7684\u8bfe\u7a0b',
            },
        ),
    ]
