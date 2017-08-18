# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django import forms
from .models import *

# 创建模型表单,根据模型Order
class   OrderCreateForm(forms.ModelForm):
    class   Meta:
        model = Order
        # 表单展示的字段，用户需要填写的内容
        fields = ['first_name', 'last_name', 'email', 'address','postal_code', 'city']


