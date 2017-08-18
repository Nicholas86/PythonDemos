# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# 1.添加商品到购物车
@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)#获取商品对象
    form = CartAddProductForm(request.POST)#初始化表单对象
    if form.is_valid():#验证表单是否合法
        cd = form.changed_data#获取表单全部数据
        print(product_id)
        cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
    return redirect('cart:cart_detail')

# 2.删除购物车商品
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

# 3.展示购物车商品
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})