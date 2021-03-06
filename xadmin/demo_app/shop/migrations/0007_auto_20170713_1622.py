# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-13 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20170713_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=555, verbose_name='\u6635\u79f0')),
                ('phone', models.CharField(max_length=255, verbose_name='\u624b\u673a\u53f7')),
                ('real_name', models.CharField(max_length=255, verbose_name='\u771f\u5b9e\u59d3\u540d')),
                ('bank_card', models.CharField(max_length=555, verbose_name='\u94f6\u884c\u5361')),
                ('sex', models.CharField(choices=[('1', '\u7537'), ('0', '\u5973')], max_length=255, verbose_name='\u6027\u522b')),
                ('age', models.SmallIntegerField(default=0, verbose_name='\u5e74\u9f84')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='\u6ce8\u518c\u65f6\u95f4')),
                ('logo', models.ImageField(upload_to='images/userlogo', verbose_name='\u5934\u50cf')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_description',
            field=models.TextField(max_length=5555, verbose_name='\u54c1\u724c\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_description',
            field=models.TextField(max_length=5555, verbose_name='\u5546\u54c1\u63cf\u8ff0'),
        ),
    ]
