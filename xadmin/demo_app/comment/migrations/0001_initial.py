# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('shop', '0016_goodsattributevalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('content', models.TextField(max_length=5555, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Goods', verbose_name='\u5546\u54c1')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.TheUser', verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba\u7ba1\u7406',
                'verbose_name_plural': '\u8bc4\u8bba\u7ba1\u7406',
            },
        ),
    ]
