#_**_encoding:utf-8_**_
import xadmin
from .models import *
class VersionAdmin(object):
    list_display = ('version', 'content','url','addtime')
    search_fields = ('version', 'content','url','addtime')
    list_filter = ('version', 'content','url','addtime')
    list_per_page = 10  # 列表分页
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面
xadmin.site.register(Version, VersionAdmin)








