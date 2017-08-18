# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.shortcuts import render
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart
# 定制管理视图
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
# Create your views here.

# 1.创建新的订单模型对象
def order_create(request):
    cart = Cart(request) #初始化购物车
    if  request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if  form.is_valid():
            order = form.save()
            # 如果数据是合法的，我们将使用order = form.save()
            # 来创建一个新的 Order实例。然后我们将会把它保存进数据库中，
            # 之后再把它保存进order变量里。
            # 在创建 order之后，我们将迭代无购车的物品然后为每个物品创建
            # OrderItem。最后，我们清空购物车。
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()#调用自定义方法
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()

    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})

# 2.定制管理站点
@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order,id=order_id)
    return render(request,'orders/order/detail.html',{'order':order})












