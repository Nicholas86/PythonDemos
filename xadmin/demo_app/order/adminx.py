#_*_encoding:utf-8_*_
from .models import *

import xadmin
#
# # 1.购物车
# class OrderXadmin(object):
#     list_display = ('id','goods_id', 'goods_name','buy_number','addtime',)
#     search_fields = ('id',)
#     list_filter = ('id','goods_id', 'goods_name','buy_number','addtime',)
#     # 这会显示一个下拉列表, 用户可以选择5秒或3600秒刷新一次页面.
#     refresh_times = (200, 3600)  # 5-10s刷新Goods页面
#     list_per_page = 10  # 列表分页
# xadmin.site.register(Order,OrderXadmin)
