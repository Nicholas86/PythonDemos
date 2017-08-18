# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# Register your models here.
from django.contrib import admin
from .models import Category,Product #注册模型到后台管理站点

class   CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

class   ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated','category']#每列展示的字段
    list_filter = ['available', 'created', 'updated']#过滤器
    search_fields = ['id','name','description']#搜索框,根据id,name产品名称,产品描述description搜索
    prepopulated_fields = {'slug': ('name',)}
    #我们在 ProductAdmin 类中使用 list_editable 属性来设置可被编辑的字段，
    # 并且这些字段都在管理站点的列表页被列出。
    # 这样可以让你一次编辑多行。任何在 list_editable 的字段也必须在 list_display 中，因为只有这样被展示的字段才可以被编辑。
    list_editable = ['price', 'stock', 'available']
admin.site.register(Product,ProductAdmin)
