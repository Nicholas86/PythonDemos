# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

# 我们商店中的目录将会由不同分类的产品组成。每一个产品会有一个名字，一段可选的描述，一张可选的图片，价格，以及库存

# 商品分类
class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="分类名称")
    slug = models.SlugField(max_length=250,db_index=True,unique=True)

    class   Meta:
        ordering = ('name',)
        verbose_name = '商品分类'
        verbose_name_plural = u'商品分类'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])#返回产品slug,product_list_by_category,需要传这个可选参数

    def __str__(self):
        return self.name

# 产品
class   Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',verbose_name='分类')#产品跟分类是多对一 的关系,一个分类下有多个产品
    name = models.CharField(max_length=200,db_index=True,verbose_name='名称')
    slug = models.SlugField(max_length=200,db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True,verbose_name='图片')
    description = models.TextField(blank=True,verbose_name='产品描述')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='价格')
    stock = models.PositiveSmallIntegerField(verbose_name='库存')
    available = models.BooleanField(default=True,verbose_name='是否可购买')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建日期')
    updated = models.DateTimeField(auto_now_add=True,verbose_name='更新日期')

    class   Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)
        verbose_name = '商品名称'
        verbose_name_plural = u'商品名称'
    # 我们使用 index_together 元选项来指定 id 和 slug 字段的共同索引。我们定义这个索引，因为我们准备使用这两个字段来查询产品，
    # 两个字段被索引在一起来提高使用双字段查询的效率。

    # 正如你已经知道的那样， get_absolute_url() 是检索一个对象的 URL 约定俗成的方法。
    # 这里，我们将使用我们刚刚在 urls.py 文件中定义的 URL 模式
    def get_absolute_url(self):
        return reverse('shop:product_detail',#product_detail重定向
                       args=[self.id, self.slug])#返回产品id,slug,因为跳转到产品详情页面product_detail,需要传这2个参数
    def __str__(self):
        return self.name

