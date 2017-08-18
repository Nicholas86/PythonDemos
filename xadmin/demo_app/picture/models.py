# _*_encoding:utf-8_*_
from __future__ import unicode_literals


from django.db import models

from django.conf import settings
USERS_THUSER_MODEL = getattr(settings, 'USERS_THUSER_MODEL', 'users.TheUser')#用户
SHOP_GOODS_MODEL = getattr(settings, 'SHOP_GOODS_MODEL', 'shop.Goods')#商品

# 自定义排序
from .fields import *
# Create your models here.

# 1.商品图片
AD_CHOICES = (
    ('0', u'回购区轮播图'),
    ('1', u'首页推荐3'),
    ('2', u'首页推荐2'),
    ('3', u'首页推荐1'),
    ('4', u'首页轮播图'),
)

IS_SHOW_CHOICES = (
    ('1',u'是'),
    ('0',u'否')
)

# 1.图片管理
class GoodsPicture(models.Model):
    goods_id = models.ForeignKey(SHOP_GOODS_MODEL,verbose_name=u'商品')
    picture = models.ImageField(upload_to='images/ScrollView',verbose_name=u'图片')
    adversitation_position = models.CharField(max_length=255,choices=AD_CHOICES,verbose_name=u'轮播图位置')
    is_show = models.CharField(max_length=255,choices=IS_SHOW_CHOICES,verbose_name=u'是否显示')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    order = OrderField(blank=True,for_fields=[])

    class Meta:
        verbose_name = u'图片管理'
        verbose_name_plural = verbose_name




