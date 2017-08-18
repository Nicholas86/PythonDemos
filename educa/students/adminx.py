# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from .models import *
from django.contrib import admin
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u"仿天猫后台管理系统"
    site_footer = u"奇维科技"
    menu_style = "accordion"
# Register your models here.
# @admin.register(OrderCourse)
# class OrderCourseAdmin(admin.ModelAdmin):
#     fields = ['course']
#     list_filter = ['course']
#     search_fields = ['course']

class OrderCourseAdmin(object):
    fields = ['course']
    list_filter = ['course']
    search_fields = ['course']
xadmin.site.register(OrderCourse,OrderCourseAdmin)


# @admin.register(Register)
# class  RegisterAdmin(admin.ModelAdmin):
#     list_display = ['name','id']
#     list_filter = ['name','id']
#     search_fields = ['name','id']

class  RegisterAdmin(object):
    list_display = ['name','id']
    list_filter = ['name','id']
    search_fields = ['name','id']
xadmin.site.register(Register,RegisterAdmin)


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

