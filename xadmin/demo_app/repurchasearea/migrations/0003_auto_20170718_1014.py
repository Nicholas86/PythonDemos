# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-18 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repurchasearea', '0002_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='discount',
            field=models.CharField(editable=False, max_length=255, verbose_name='\u4f18\u60e0\u6bd4\u4f8b'),
        ),
    ]