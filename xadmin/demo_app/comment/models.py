#_**_coding:utf-8_**_
from __future__ import unicode_literals

from django.db import models

from django.conf import settings
USERS_THUSER_MODEL = getattr(settings, 'USERS_THUSER_MODEL', 'users.TheUser')#用户
SHOP_GOODS_MODEL = getattr(settings, 'SHOP_GOODS_MODEL', 'shop.Goods')#商品

# 1.评论
class Comment(models.Model):
    goods_id = models.ForeignKey(SHOP_GOODS_MODEL,verbose_name=u'商品')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'评论时间')
    user_id = models.ForeignKey(USERS_THUSER_MODEL,verbose_name=u'用户')
    content = models.TextField(max_length=5555, verbose_name=u'评论内容')

    class Meta:
        verbose_name = u'评论管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content