# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from decimal    import Decimal
from django.conf    import settings
from shop.models import Product #从商品应用shop，导入商品Product模型

#创建Cart类
class   Cart(object):
    # 我们需要把购物车与一个 request 对象一同初始化
    def __init__(self,request):
        """
        Initialize the cart.
        :param request:
        """
        #使用self.session = request.session保存会话以便使其对Cart类的其他方法可用。
        self.session = request.session
        cart_session = self.session.get(settings.CART_SESSION_ID)
        if not cart_session:
            # save an empty cart in the session
            # 如果当前会话中没有购物车，我们就在会话中设置一个空字典，这样就可以在会话中设置一个空的购物车。
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart_session = cart_session #定义全部变量self.cart保存购物车会话


    # 1.添加产品方法
    """
    参数:product,quantity,update_quantity
    """
    def add(self,product, quantity=1, update_quantity=False):
        # 我们在购物车字典中把产品,id作为键。我们把产品id转换为字符串，因为 Django使用 JSON 来序列化会话数据，
        # 而JSON又只接受字符串的键名。产品id为键，一个有quantity和price的字典作为值。
        product_id = str(product.id)
        print('---2 商品id --- %d'%(product_id))
        if  product_id not  in  self.cart_session:
            self.cart_session[product_id] = { 'quantity': 0,'price': str(product.price)}
        if update_quantity:
            self.cart_session[product_id]['quantity'] = quantity
        else:
            self.cart_session[product_id]['quantity'] += quantity

        self.save()

    # 2.方法会把购物车中所有的改动都保存到会话中，
    # 然后用 session.modified = True 标记改动了的会话。
    # 这是为了告诉 Django 会话已经被改动，需要将它保存起来
    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart_session
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True


    #3.删除购物中的指定商品
    def remove(self,product):
        product_id = str(product.id)
        if  product_id in self.cart_session:
            del self.cart_session[product_id]
            self.save()#然后调用 save() 方法来更新会话中的购物车。

    # 4.我们将迭代购物车当中的物品，然后获取相应的 Product 实例。
    # 为恶劣达到我们的目的，你需要定义 __iter__() 方法。把下列代码添加进 Cart 类中：
    def __iter__(self):
        product_ids = self.cart_session.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(category_id__in=product_ids)
        for product in products:
            self.cart_session[str(product.id)]['product'] = product

        for item in self.cart_session.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # 5.当len() 方法在一个对象上执行时，Python会调用对象的__len__()方法来检索它的长度。
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart_session.values())

    # 6.添加下列方法来计算购物车中物品的总价：
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart_session.values())

    # 7.最后，添加一个方法来清空购物车会话：
    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True







