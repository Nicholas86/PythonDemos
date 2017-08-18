# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from rest_framework import serializers
from .models import *

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Register
        # Meta类允许你去指定模型序列化以及给序列化包含的字段。
        # 所有的模型字段都会被包含如果你没有设置一个fields属性。
        fields = ('id','name','password')
        # fields = '__all__' #返回所有字段




