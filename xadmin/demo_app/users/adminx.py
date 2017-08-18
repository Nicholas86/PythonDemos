# _*_encoding:utf-8_*_

import xadmin
from .models import *

#1.用户(信息)注册
class UserXadmin(object):
    list_display = ('nickname', 'phone','real_name','bank_card','sex','age','addtime',)
    search_fields = ('nickname', 'phone','real_name','bank_card','sex','age','addtime',)
    list_filter = ('nickname', 'phone','real_name','bank_card','sex','age','addtime',)
xadmin.site.register(TheUser,UserXadmin)


# 2.地址
class AddressXadmin(object):
    list_display = ('consignee_name','consignee_address', 'consignee_telphone','addtime',)
    search_fields = ('consignee_name','consignee_address',)
    list_filter = ('consignee_name','consignee_address', 'consignee_telphone','addtime',)
    # 这会显示一个下拉列表, 用户可以选择5秒或3600秒刷新一次页面.
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面
    list_per_page = 10  # 列表分页
xadmin.site.register(Address,AddressXadmin)


# 3.收藏
class CollectionXadmin(object):
    list_display = ('id', 'user_id', 'goods_name', 'goods_price','market_price','addtime',)
    search_fields = ('id', 'goods_name',)
    list_filter = ('id', 'user_id', 'goods_name', 'goods_price','market_price','addtime',)
    # 这会显示一个下拉列表, 用户可以选择5秒或3600秒刷新一次页面.
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面
    list_per_page = 10  # 列表分页

xadmin.site.register(Collection, CollectionXadmin)






