# _*_coding:utf-8_*_
from __future__ import unicode_literals

from django.db import models

from django.conf import settings
USERS_THUSER_MODEL = getattr(settings, 'USERS_THUSER_MODEL', 'users.TheUser')#用户

# Create your models here.

# 1.我要买
class Buy(models.Model):
    user_id = models.ForeignKey(USERS_THUSER_MODEL, verbose_name=u'用户')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    content = models.TextField(max_length=5555, verbose_name=u'求购信息')

    class Meta:
        verbose_name = u'我要买'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

# 2.我要卖
IS_OK_CHOICES = (
    ('0','否'),
    ('1','是'),
)
# editable = False 设为False,xadmin将不会出现在管理站点上
class Sale(models.Model):
    user_id = models.ForeignKey(USERS_THUSER_MODEL, verbose_name=u'用户')
    goods_name = models.CharField(max_length=255,verbose_name=u'商品名称')
    goods_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'商品价格')
    market_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'市场价')
    goods_tag = models.CharField(max_length=2555,verbose_name=u'商品标签')
    goods_picture = models.ImageField(upload_to='images/Sale',verbose_name=u'商品图片')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    is_ok = models.CharField(max_length=255,choices=IS_OK_CHOICES,verbose_name=u'是否通过审核')
    discount = models.CharField(max_length=255,editable = False,verbose_name=u'优惠比例')#不显示在xadmin上
    goods_description = models.TextField(max_length=5555, verbose_name=u'商品描述')

    class Meta:
        verbose_name = u'我要卖'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_description