# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.db import models
# Create your models here.
from shop.models import Product

# Order 模型包含几个用户信息的字段和一个 paid 布尔值字段，这个字段默认值为 False 。
# 待会儿，我们将使用这个字段来区分支付和未支付订单。
# 我们也定义了一个 get_total_cost() 方法来得到订单中购买物品的总花费。
# 1.订单模型
class   Order(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='姓')
    last_name = models.CharField(max_length=50,verbose_name='名')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=250,verbose_name='地址')
    postal_code = models.CharField(max_length=20,verbose_name='邮政编码')
    city = models.CharField(max_length=100,verbose_name='城市')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    paid = models.BooleanField(default=False,verbose_name='是否支付')

    class   Meta:
        ordering = ('-created',)
        verbose_name = u'订单'
        verbose_name_plural = u'订单'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


# OrderItem 模型让我们可以保存物品，数量和每个物品的支付价格。
# 2.我们引用 get_cost() 来返回物品的花费。
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',verbose_name='订单')
    product = models.ForeignKey(Product,related_name='order_items',verbose_name='商品')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='价格')
    quantity = models.PositiveIntegerField(default=1,verbose_name='数量')

    class   Meta:
        verbose_name = u'物品'
        verbose_name_plural = u'物品'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity










