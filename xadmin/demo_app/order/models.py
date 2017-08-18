#_*_encoding:utf-8_*_
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
USERS_THUSER_MODEL = getattr(settings, 'USERS_THUSER_MODEL', 'users.TheUser')#用户
SHOP_GOODS_MODEL = getattr(settings, 'SHOP_GOODS_MODEL', 'shop.Goods')#商品

# Create your models here.

# # 1.订单
# class Order(models.Model):
#     user_id = models.ForeignKey(USERS_THUSER_MODEL, verbose_name=u'用户')
#     goods_id = models.ForeignKey(SHOP_GOODS_MODEL,verbose_name=u'商品')
#     goods_name = models.CharField(max_length=5555, verbose_name=u'商品名称')
#     goods_price = models.CharField(max_length=255, verbose_name=u'商品价格')
#     buy_number = models.IntegerField(default=0, verbose_name=u'购买数量')
#     addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
#
#     class Meta:
#         verbose_name = u'订单管理'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return '{}.{}'.format(self.goods_name, self.goods_price)