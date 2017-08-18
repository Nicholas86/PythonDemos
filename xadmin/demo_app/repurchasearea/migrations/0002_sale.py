# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_address_user_id'),
        ('repurchasearea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=255, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u5546\u54c1\u4ef7\u683c')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u5e02\u573a\u4ef7')),
                ('goods_tag', models.CharField(max_length=2555, verbose_name='\u5546\u54c1\u6807\u7b7e')),
                ('goods_picture', models.ImageField(upload_to='images/Sale', verbose_name='\u5546\u54c1\u56fe\u7247')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('is_ok', models.CharField(choices=[('0', '\u5426'), ('1', '\u662f')], max_length=255, verbose_name='\u662f\u5426\u901a\u8fc7\u5ba1\u6838')),
                ('discount', models.CharField(max_length=255, verbose_name='\u4f18\u60e0\u6bd4\u4f8b')),
                ('goods_description', models.TextField(max_length=5555, verbose_name='\u5546\u54c1\u63cf\u8ff0')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.TheUser', verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u6211\u8981\u5356',
                'verbose_name_plural': '\u6211\u8981\u5356',
            },
        ),
    ]
