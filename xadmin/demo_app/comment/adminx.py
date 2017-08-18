#_**_coding:utf-8_**_
import xadmin
from .models import *

# 评论
class CommentAdmin(object):
    list_display = ( 'goods_id','content','addtime','user_id',)
    search_fields = ( 'goods_id','content','addtime','user_id',)
    list_filter = ( 'goods_id','content','addtime','user_id',)
    list_per_page = 10 #列表分页
    refresh_times = (200, 3600)#5-10s刷新Goods页面
xadmin.site.register(Comment,CommentAdmin)
