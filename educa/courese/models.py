# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.db import models
from django.contrib.auth.models import User
# 通用模型内容
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import *
# Create your models here.

# 1.科目模型(音乐)
class   Subject(models.Model):
    title = models.CharField(max_length=200,verbose_name='科目名字')
    slug = models.SlugField(max_length=200,verbose_name='slug',unique=True)

    class   Meta:
        verbose_name = '科目'
        verbose_name_plural = u'科目'
        ordering = ('-title',)#以标题降序

    def __str__(self):
        return self.title

# 2.课程（大一音乐,大二音乐）
class   Course(models.Model):
    owner = models.ForeignKey(User,related_name='courses_created',verbose_name='课程创建人')#课程的拥有者
    subject = models.ForeignKey(Subject,related_name='courses',verbose_name='科目')#课程属于哪个科目
    title = models.CharField(max_length=200,verbose_name='课程名称')
    slug = models.SlugField(max_length=200,verbose_name='slug',unique=True)
    overview = models.TextField(verbose_name='课程概述')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class   Meta:
        verbose_name = '课程'
        verbose_name_plural = u'课程'
        ordering = ('-created',)

    def __str__(self):
        return self.title

# 3.模块(大一音乐,下面有2个部分,第一部分,第二部分)
class   Module(models.Model):
    course = models.ForeignKey(Course,related_name='modules',verbose_name='课程')
    title = models.CharField(max_length=200,verbose_name='模块(部分)标题')
    description = models.TextField(blank=True,verbose_name='模块(部分)描述')#允许空白
    order = OrderField(blank=True,for_fields=['course'])
    class   Meta:
        verbose_name = u'课程管理的模块(部分)'
        verbose_name_plural = u'课程管理的模块(部分)'
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

 # 4.(文本,图片,视频,)里面添加内容
# 我们的courses应用的Content模型包含一个通用关系来连接不同类型的内容给该应用。
# 我们将要创建一个不同的模型给每种类型的内容。所有内容模型将会有一些公用的字段，以及额外的字段去存储定制数据。
class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', verbose_name='模块(部分)')
    order = OrderField(blank=True, for_fields=['module'], verbose_name='次序(自定义模型字段排序用)')
    # 请记住，我们需要三种不同的字段来设置一个通用关系
    content_type = models.ForeignKey(ContentType, verbose_name='内容类型',
                                     limit_choices_to={'model__in': ('text', 'video', 'image', 'file')})
                                    # 一个ForeignKey字段指向ContentType模型
    # 这是PositiveIntegerField用来存储有关联对象的关键字
    object_id = models.PositiveIntegerField(verbose_name='有关联对象关键字')
    # 一个GenericForeignKey字段指向被关联的对象通过结合前两个字段
    item = GenericForeignKey('content_type', 'object_id')
    content = models.CharField(max_length=2000, verbose_name='为(文本,图片,视频,文件)添加内容', blank=True)

    class Meta:
        verbose_name = '内容'
        verbose_name_plural = u'内容'
        ordering = ['order']  # 按order排序

    def __str__(self):
        return str(self.content)
        # 只有content_type和object_id字段有一个对应列在这个模型的数据库表中。
        # item字段允许你去检索或者直接设置关联对象，并且它的功能是建立在其他两个字段之上。


# 5.
# 我们将会创建一个抽象模型来提供公用字段给所有内容模型。
# 一个抽象模型就是一个基础类，你定义在其中的字段就是你想要包含到所有子模型中的字段。
# Djnago不会创建任何数据库表给抽象模型。
# 每个子模型都会创建一张数据库表，包含有继承自抽象类的字段以及在子模型中自己定义的字段。
# 为了创建子模型，你只需要基于这个抽象模型

class   ItemBase(models.Model):
    owner = models.ForeignKey(User,related_name='%(class)s_related',verbose_name='创建人')
    module = models.ForeignKey(Module,verbose_name='模块')
    title = models.CharField(max_length=250,verbose_name='内容标题')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class   Meta:
        abstract = True
        #为了抽象一个模型，你需要在Meta类中包含abstract=True。Django将会认出这个模型是一个抽象模型并且不会给它创建数据库表
    def __str__(self):
        return self.title

class Text(ItemBase):
    content = models.TextField(verbose_name='文本')

    class   Meta:
        verbose_name = u'文本'
        verbose_name_plural = u'文本'


class File(ItemBase):
    file = models.FileField(upload_to='files',verbose_name='文件')

    class   Meta:
        verbose_name = u'文件'
        verbose_name_plural = u'文件'


class Image(ItemBase):
    file = models.FileField(upload_to='images',verbose_name='图片')

    class   Meta:
        verbose_name = u'图片'
        verbose_name_plural = u'图片'


class Video(ItemBase):
    url = models.URLField(verbose_name='视频')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = u'视频'


#学生
class Student(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=200)
    gender = models.IntegerField(verbose_name='性别')
    class Meta:
        verbose_name_plural = u'学生'
        verbose_name = u'学生'
    def __str__(self):
        return self.name


