# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.shortcuts import render,get_object_or_404

from .models import Category,Product

from cart.forms import CartAddProductForm

# Create your views here.
# 商品列表
def  product_list(request,category_slug=None):
     # category_slug 可选参数
     category = None
     categories = Category.objects.all()
     products = Product.objects.filter(available=True)

     if category_slug:
         category = get_object_or_404(Category,slug = category_slug)#根据slug获取Category分类对象
         products = products.filter(category = category)

     return render(request,
                  'shop/product/list.html',
                  {'category': category,
                  'categories': categories,
                  'products': products})

# 我们也需要一个视图来检索和展示单一的产品。把下面的代码添加进去：
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    # 把CartAddProductForm 添加进product_detail视图中
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,'cart_product_form': cart_product_form})







