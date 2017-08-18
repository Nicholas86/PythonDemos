# _*_coding:utf-8_*_
from __future__ import unicode_literals
from django.db import models


from django.conf import settings
USERS_THUSER_MODEL = getattr(settings, 'USERS_THUSER_MODEL', 'users.TheUser')#用户
SHOP_GOODS_MODEL = getattr(settings, 'SHOP_GOODS_MODEL', 'shop.Goods')#商品
# Create your models here.

#1.用户(信息)注册
Sex_Choices = (
    ('1','男'),
    ('0','女'),
)
class  TheUser(models.Model):
    nickname = models.CharField(max_length=555,verbose_name=u'昵称')
    phone = models.CharField(max_length=255,verbose_name=u'手机号')
    password = models.CharField(max_length=555,verbose_name=u'密码')
    real_name = models.CharField(max_length=255,verbose_name=u'真实姓名')
    bank_card = models.CharField(max_length=555,verbose_name=u'银行卡')
    sex = models.CharField(max_length=255,default=0,choices=Sex_Choices,verbose_name=u'性别')
    age = models.SmallIntegerField(default=0,verbose_name=u'年龄')#默认女
    addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'注册时间')
    logo = models.ImageField(upload_to='images/Userlogo',verbose_name=u'头像')

    class Meta:
        verbose_name = u'用户管理'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{}.{}'.format(self.nickname,self.phone)

# 2.地址
class Address(models.Model):
    user_id = models.ForeignKey(TheUser,verbose_name=u'用户')
    consignee_address = models.CharField(max_length=5555,verbose_name=u'收货人地址')
    consignee_telphone = models.CharField(max_length=255,verbose_name=u'手机号')
    consignee_name = models.CharField(max_length=255,verbose_name=u'收货人姓名')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'地址管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}.{}'.format(self.consignee_name, self.consignee_telphone)

# 3.收藏
class Collection(models.Model):
    user_id = models.ForeignKey(USERS_THUSER_MODEL, verbose_name=u'用户')
    goods_id = models.ForeignKey(SHOP_GOODS_MODEL,verbose_name=u'商品')
    goods_name = models.CharField(max_length=5555, verbose_name=u'商品名称')
    goods_price = models.CharField(max_length=255, verbose_name=u'商品价格')
    market_price = models.CharField(max_length=255, verbose_name=u'市场价')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'收藏时间')

    class Meta:
        verbose_name = u'收藏管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}.{}'.format(self.goods_name, self.goods_price)




















