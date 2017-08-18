# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

class   CouponAdmin(admin.ModelAdmin):
    list_filter = ['code', 'valid_from', 'valid_to','discount', 'active']
    list_display = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']
admin.site.register(Coupon,CouponAdmin)
