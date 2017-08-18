# _*_coding:utf-8_*_

import xadmin
from .models import *


# 1.分类
@xadmin.sites.register(Category)
class CategoryXadmin(object):
    list_display = ('name','addtime','order',)
    search_fields = ('name','addtime','order',)
    list_filter = ('name','addtime','order',)
    list_per_page = 10  # 列表分页
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面


# 2.类型
# 内联属性
class AttributeInline(object):
    model = Attribute
    extra = 0

class  TypeXadmin(object):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    list_per_page = 10 #列表分页
    refresh_times = (200, 3600)#5-10s刷新Goods页面
    inlines = [AttributeInline]
xadmin.site.register(Type,TypeXadmin)


# 3.属性
class AttributeXadmin(object):
    list_display = ('name','type_id','option_value')
    search_fields = ('name','type_id','option_value')
    list_filter = ('name','type_id','option_value')
    list_per_page = 10 #列表分页
    refresh_times = (200, 3600)#5-10s刷新Goods页面
xadmin.site.register(Attribute,AttributeXadmin)

# 4.品牌
class BrandXadmin(object):
    list_display = ('name','addtime','brand_description',)
    search_fields = ('name','addtime','brand_description',)
    list_filter = ('name', 'addtime','brand_description',)
    list_per_page = 10 #列表分页
    refresh_times = (200, 3600)#5-10s刷新Goods页面
xadmin.site.register(Brand,BrandXadmin)


# 5.商品
class GoodsXadmin(object):
    list_display = ('name','category_id' ,'brand_id','goods_description','market_price',
                    'shop_price','goods_sale_number','is_on_sale','addtime',
                    'is_new','is_recommand','goods_stock_number',)
    # search_fields = ('name','category_id' ,'brand_id','goods_description','market_price',
    #                 'shop_price','goods_sale_number','is_on_sale','addtime',
    #                 'is_new','is_recommand','goods_stock_number',)
    search_fields = ('name','is_new',)
    list_filter = ('name','category_id' ,'brand_id','goods_description','market_price',
                    'shop_price','goods_sale_number','is_on_sale','addtime',
                    'is_new','is_recommand','goods_stock_number',)
    # 这会显示一个下拉列表, 用户可以选择5秒或3600秒刷新一次页面.
    refresh_times = (200, 3600)#5-10s刷新Goods页面
    list_per_page = 10 #列表分页
xadmin.site.register(Goods,GoodsXadmin)


# 6.商品属性值
class GoodsAttributeValueXadmin(object):
    list_display = ('attribute_value', 'attribute_price', 'attribute_id', 'goods_id',)
    search_fields = ('attribute_value', 'attribute_price', 'attribute_id', 'goods_id',)
    list_filter = ('attribute_value', 'attribute_price', 'attribute_id', 'goods_id',)
    # 这会显示一个下拉列表, 用户可以选择5秒或3600秒刷新一次页面.
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面
    list_per_page = 10  # 列表分页
xadmin.site.register(GoodsAttributeValue, GoodsAttributeValueXadmin)










