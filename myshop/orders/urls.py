# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^create/$',views.order_create,name='order_create'),
        url(r'^admin/orders/order/(?P<order_id>\d+)/$',views.admin_order_detail,name='admin_order_detail'),
]
