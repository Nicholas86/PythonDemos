#_*_encoding:utf-8_*_

from django.contrib import admin
import xadmin
from .models import *
# Register your models here.

# 1.图片
class GoodsPictureXadmin(object):
    list_display = ('goods_id', 'picture', 'adversitation_position', 'is_show','addtime','order')
    search_fields = ('id',)
    list_filter = ('goods_id', 'picture', 'adversitation_position', 'is_show','addtime','order')
    # 这会显示一个下拉列表, 用户可以选择5秒或3600秒刷新一次页面.
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面
    list_per_page = 10  # 列表分页
xadmin.site.register(GoodsPicture, GoodsPictureXadmin)