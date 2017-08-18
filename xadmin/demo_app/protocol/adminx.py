#_**_encoding:utf-8_**_

import xadmin
from .models import *
# 1.协议
class ProtocolAdmin(object):
    list_display = ('content','addtime',)
    search_fields = ('content','addtime',)
    list_filter = ('content','addtime',)
    list_per_page = 10 #列表分页
    refresh_times = (200, 3600)#5-10s刷新Goods页面
xadmin.site.register(Protocol,ProtocolAdmin)



