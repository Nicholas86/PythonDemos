# -*- coding: utf-8 -*-


from django.conf.urls   import url
from .views import *

urlpatterns = [
    url(r'^$', product_list, name='product_list'),
    # 带参数category_slug商品分类的slug
    url(r'^product_list/(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
    url(r'^product_detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),
    ]
