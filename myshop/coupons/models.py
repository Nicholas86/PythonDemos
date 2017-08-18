# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator,MaxValueValidator

# 优惠券模型
class   Coupon(models.Model):
    code = models.CharField(max_length=50,verbose_name='优惠码',unique=True)
    valid_from = models.DateTimeField(verbose_name='生效时间')
    valid_to = models.DateTimeField(verbose_name='过期时间')
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name='折扣率')
    active = models.BooleanField(verbose_name='是否激活')

    class   Meta:
        verbose_name_plural = u'优惠券'
        verbose_name = '优惠券'

    def __str__(self):
        return self.code

