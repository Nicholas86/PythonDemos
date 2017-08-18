# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


from django.conf.urls   import url
from .views import *

urlpatterns = [
    url(r'^$', cart_detail, name='cart_detail'),#name='cart_detail'重定向用
    url(r'^add/(?P<product_id>\d+)/$',cart_add,name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$',cart_remove,name='cart_remove'),
]


