# _*_coding:utf-8_*_

import xadmin
from .models import *

# 1.我要买
class BuyXadmin(object):
    list_display = ( 'id','user_id','content','addtime',)
    search_fields = ( 'id',)
    list_filter = ( 'id','user_id','content','addtime',)
    list_per_page = 10 #列表分页
    refresh_times = (200, 3600)#5-10s刷新Goods页面
xadmin.site.register(Buy,BuyXadmin)

# 2.我要卖
class SaleXadmin(object):
    list_display = ('id', 'goods_picture','user_id', 'goods_name',
                    'goods_price','market_price','goods_tag','addtime',
                    'discount','goods_description',
                    )
    search_fields = ('id',)
    list_filter = ('id', 'goods_picture','user_id', 'goods_name',
                    'goods_price','market_price','goods_tag','addtime',
                    'discount','goods_description',
                    )
    list_per_page = 10  # 列表分页
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面
xadmin.site.register(Sale, SaleXadmin)
