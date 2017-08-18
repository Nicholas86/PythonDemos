# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 我们会在api目录中构建所有的API功能
from rest_framework import serializers
from ..models import *

#     Serializer：给一般的Python类实例提供序列化。
#     ModelSerializer：给模型实例提供序列化。
#     HyperlinkedModelSerializer：类似与ModelSerializer，但是代表与链接而不是主键的对象关系。

# 1.Subject科目序列化器
class   SubjectSerializer(serializers.ModelSerializer):
    # Meta类允许你去指定模型序列化以及给序列化包含的字段。
    # 所有的模型字段都会被包含如果你没有设置一个fields属性。
    class   Meta:
        model = Subject
        fields = ('id', 'title', 'slug')


# 2.Module模块
class ModuleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Module
            # Meta类允许你去指定模型序列化以及给序列化包含的字段。
            # 所有的模型字段都会被包含如果你没有设置一个fields属性。
            # fields = ('order', 'title', 'description')
            fields = '__all__' #返回Module模型(数据库)所有字段


# 3.Course课程模型序列化
class   CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    class   Meta:
        model = Course
        # Meta类允许你去指定模型序列化以及给序列化包含的字段。
        # 所有的模型字段都会被包含如果你没有设置一个fields属性。
        fields = ('id', 'subject', 'title', 'slug','overview','created', 'owner', 'modules')#返回Course(数据库)模型指定字段

# 4.Content内容模型序列化
class   ContentSerializer(serializers.ModelSerializer):
    class   Meta:
        model = Content
        fields = '__all__'


# 5.ContentType模型序列化text,image
class   ContentTypeSerializer(serializers.ModelSerializer):
        class Meta:
            model = ContentType
            fields = '__all__'

# 6.Text模型序列化
class TextSerializer(serializers.ModelSerializer):
        class Meta:
            model = Text
            fields = '__all__'

# 7.Video模型序列化
class VideoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Video
            fields = '__all__'

# 8.File模型序列化
class FileSerializer(serializers.ModelSerializer):
        class Meta:
            model = File
            fields = '__all__'

# 9.Image模型序列化
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'






