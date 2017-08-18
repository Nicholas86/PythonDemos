# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.contrib import admin

# Register your models here.
from .models import *
from django.core.urlresolvers import reverse
# 内联
class   OrderItemInline(admin.TabularInline):
    # 我们在OrderItem使用ModelInline来把它引用为OrderAdmin
    # 类的内联元素。一个内联元素允许你在同一编辑页引用模型，并且将这个模型作为父模型
    model = OrderItem
    raw_id_fields = ['product']

def order_detail(obj):
    return '<a href="{}">视图</a>'.format(reverse('orders:admin_order_detail', args=[obj.id]))
order_detail.allow_tags = True


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated',order_detail]
    list_filter = ['paid', 'created', 'updated']

    inlines = [OrderItemInline]#将OrderItemInline引为内联

admin.site.register(Order, OrderAdmin)
