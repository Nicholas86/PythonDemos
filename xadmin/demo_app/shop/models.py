#_*_encoding:utf8_*_

from __future__ import unicode_literals

from django.db import models

# 自定义排序
from .fields import *

# Create your models here.

# 1.分类
class  Category(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'分类名称')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'添加时间')
    order = OrderField(blank=True,for_fields=[])

    class Meta:
        verbose_name = u'分类管理'
        verbose_name_plural = verbose_name
        # ordering = ('-addtime',)
    def __str__(self):
        return  '{}.{}'.format(self.name,self.order)

# 2.类型
class Type(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'类型名称')

    class Meta:
        verbose_name = u'类型管理'
        verbose_name_plural = verbose_name
    # ordering = ('-addtime',)
    def __str__(self):
        return '{}'.format(self.name,)


# 3.属性
class Attribute(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'属性名称')
    type_id = models.ForeignKey(Type, verbose_name=u'类型')
    option_value = models.CharField(max_length=5555,verbose_name=u'属性值')

    class Meta:
        verbose_name = u'属性管理'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{}'.format(self.name)


# 4.品牌
class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'品牌名称')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    logo = models.ImageField(upload_to='images/Logo', verbose_name=u'商标')  # 需要沟通
    small_logo = models.CharField(max_length=255, verbose_name=u'logo缩略图')  # 需要沟通
    order = OrderField(blank=True, for_fields=[], verbose_name=u'排序')
    brand_description = models.TextField(max_length=5555, verbose_name=u'品牌描述')

    class Meta:
        verbose_name = u'品牌管理'
        verbose_name_plural = verbose_name
        # ordering = ('-addtime',)
    def __str__(self):
        return '{}.{}'.format(self.name, self.order)


# 5.商品
class Goods(models.Model):
    category_id = models.ForeignKey(Category,verbose_name='分类')
    type_id = models.ForeignKey(Type,verbose_name=u'类型')
    brand_id = models.ForeignKey(Brand,verbose_name=u'品牌')
    name = models.CharField(max_length=360,verbose_name=u'商品名称')
    market_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'市场价格')
    shop_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'本店价格')
    goods_sale_number = models.BigIntegerField(editable=False,verbose_name=u'销售量')#不显示在xadmin上
    is_on_sale = models.BooleanField(default=0,verbose_name=u'是否上架')#1上架,0下架
    addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'添加时间')
    is_new = models.BooleanField(default=0,verbose_name=u'是否新品')#1新品,0旧品
    is_recommand = models.BooleanField(default=0,verbose_name=u'是否推荐')#1.推荐,0不推荐
    goods_stock_number = models.BigIntegerField(verbose_name=u'库存量')
    order = OrderField(blank=True, for_fields=[],verbose_name=u'排序')
    goods_description = models.TextField(max_length=5555,verbose_name=u'商品描述')

    class Meta:
        verbose_name = u'商品管理'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

# 6.商品属性值
class GoodsAttributeValue(models.Model):
    goods_id = models.ForeignKey(Goods,verbose_name=u'商品')
    attribute_id = models.ForeignKey(Attribute,verbose_name=u'商品属性')
    attribute_value = models.CharField(max_length=255,verbose_name=u'属性值')
    attribute_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'属性价格')

    class Meta:
        verbose_name = u'属性值'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.attribute_value






