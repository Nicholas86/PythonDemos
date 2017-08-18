# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.contrib import admin

#导入xadmin管理后台站点
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from .models import *


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u"仿天猫后台管理系统"
    site_footer = u"奇维科技"
    menu_style = "accordion"


#  Register your models here.
# 注册到管理平台

# 1.科目
# 我们使用@admin.register()装饰器替代了admin.site.register()方法。它们都提供了相同的功能。
# @admin.register(Subject)
# class    SubjectAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slug']
#     prepopulated_fields = {'slug': ('title',)}
#     list_filter = ['title', 'slug']
#     search_fields = ['title']


class    SubjectAdmin(object):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['title', 'slug']
    search_fields = ['title']
xadmin.site.register(Subject,SubjectAdmin)

# 2.模块内联
# class ModuleInline(admin.StackedInline):
#     model = Module #内联

class ModuleInline(object):
    model = Module #内联
    extra = 0
# 3.课程
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['title', 'subject', 'created','id']
#     list_filter = ['created', 'subject']
#     search_fields = ['title', 'overview']
#     prepopulated_fields = {'slug': ('title',)}
#     inlines = [ModuleInline]#内联模型,编辑课程界面的shih,可以同时编辑模块

class CourseAdmin(object):
    list_display = ['title', 'subject', 'created','id']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]#内联模型,编辑课程界面的shih,可以同时编辑模块
xadmin.site.register(Course,CourseAdmin)

# 内联内容
# class   ContentInline(admin.StackedInline):
#     model = Content#写在上面,这样下面用,不报错

class   ContentInline(object):
    model = Content#写在上面,这样下面用,不报错
    extra = 0

# 4.模块注册
# @admin.register(Module)
# class   ModuleAdmin(admin.ModelAdmin):
#     list_display = ['course','title','description','order','id']
#     list_filter = ['title']
#     inlines = [ContentInline]#模块内联内容模型Content

class   ModuleAdmin(object):
    list_display = ['course','title','description','order','id']
    list_filter = ['title']
    inlines = [ContentInline]#模块内联内容模型Content
xadmin.site.register(Module,ModuleAdmin)


# 5.注册学生模型
# @admin.register(Student)
# class   StudentAdmin(admin.ModelAdmin):
#     list_display = ['name','gender','id']
#     search_fields = ['name','id']
#     list_filter = ['name','gender']

class   StudentAdmin(object):
    list_display = ['name','gender','id']
    search_fields = ['name','id']
    list_filter = ['name','gender']
admin.site.register(Student,StudentAdmin)


# 6.注册内容模型
# @admin.register(Content)
# class   ContentAdmin(admin.ModelAdmin):
#     list_display = ['content','order','object_id','item','content_type']#不要content_type
#     list_filter = ['content','order','object_id']#不要content_type
#     search_fields = ['content','order','object_id','content_type']#不要content_type
class   ContentAdmin(object):
    list_display = ['content','order','object_id','item','content_type']#不要content_type
    list_filter = ['content','order','object_id']#不要content_type
    search_fields = ['content','order','object_id','content_type']#不要content_type
xadmin.site.register(Content,ContentAdmin)


# 7.注册文本模型
# @admin.register(Text)
# class   TextAdmin(admin.ModelAdmin):
#     list_display = ['content', 'owner', 'title','created','updated','module']
#     list_filter = ['content', 'owner', 'title','created','updated','module']
#     search_fields = ['content', 'owner', 'title','created','updated','module']

class   TextAdmin(object):
    list_display = ['content', 'owner', 'title','created','updated','module']
    list_filter = ['content', 'owner', 'title','created','updated','module']
    search_fields = ['content', 'owner', 'title','created','updated','module']
xadmin.site.register(Text,TextAdmin)


# 8.注册文件模型
# @admin.register(File)
# class   FileAdmin(admin.ModelAdmin):
#     list_display = ['file', 'owner', 'title','created','updated','module']
#     list_filter = ['file', 'owner', 'title','created','updated','module']
#     search_fields = ['file', 'owner', 'title','created','updated','module']

class   FileAdmin(object):
    list_display = ['file', 'owner', 'title','created','updated','module']
    list_filter = ['file', 'owner', 'title','created','updated','module']
    search_fields = ['file', 'owner', 'title','created','updated','module']
xadmin.site.register(File,FileAdmin)

# 9.注册图片模型
# @admin.register(Image)
# class   ImageAdmin(admin.ModelAdmin):
#     list_display = ['file', 'owner', 'title','created','updated','module']
#     list_filter = ['file', 'owner', 'title','created','updated','module']
#     search_fields = ['file', 'owner', 'title','created','updated','module']

class   ImageAdmin(object):
    list_display = ['file', 'owner', 'title','created','updated','module']
    list_filter = ['file', 'owner', 'title','created','updated','module']
    search_fields = ['file', 'owner', 'title','created','updated','module']
xadmin.site.register(Image,ImageAdmin)

# 10.注册视频模型
# @admin.register(Video)
# class   VideoAdmin(admin.ModelAdmin):
#     list_display = ['url', 'owner', 'title','created','updated','module']
#     list_filter = ['url', 'owner', 'title','created','updated','module']
#     search_fields = ['url', 'owner', 'title','created','updated','module']

class   VideoAdmin(object):
    list_display = ['url', 'owner', 'title','created','updated','module']
    list_filter = ['url', 'owner', 'title','created','updated','module']
    search_fields = ['url', 'owner', 'title','created','updated','module']
xadmin.site.register(Video,VideoAdmin)


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

