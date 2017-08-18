# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courese', '0003_auto_20170616_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u59d3\u540d')),
                ('gender', models.IntegerField(verbose_name='\u6027\u522b')),
            ],
            options={
                'verbose_name': '\u5b66\u751f',
                'verbose_name_plural': '\u5b66\u751f',
            },
        ),
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courese.Course', verbose_name='\u8bfe\u7a0b'),
        ),
    ]
