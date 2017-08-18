# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PRODUCT_QUANTITY_CHOICES = [(i, int(i)) for i in range(1, 21)]

class  CartAddProductForm(forms.Form):

    # 用户输入的数量
    # quantity = forms.TypedChoiceField(
    #     choices=PRODUCT_QUANTITY_CHOICES,
    #     coerce=int)
    quantity = forms.IntegerField(max_value=2000)
    # 是否更新
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

