# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from . import views
from django.conf.urls   import url,include
# 2.rest_framewor框架
from rest_framework  import routers
from rest_framework.urlpatterns import format_suffix_patterns

import students.views
#初始化路由对象
router = routers.DefaultRouter()
router.register(r'subjectRouter',views.SubjectViewSet)#1.科目列表,通过路由访问
router.register(r'subjectViewModelViewRouter',views.SubjectViewModelViewSet)#2.科目列表
router.register(r'coureseViewModelViewRouter',views.CourseViewModelViewSet)#3.课程列表
router.register(r'coureseDetailViewModelRouter',views.CoureseDetailViewModelRouter)#4.课程详情
router.register(r'registerModelViewSetRouter',views.RegisterModelViewSet)#5.注册
router.register(r'loginModelViewSetRouter',views.LoginModelViewSet)#6.登录
router.register(r'updateCoureseDetailRouter',views.UpdateCoureseDetailModuleViewModelViewSet)#7.更新课程模块
router.register(r'addCoureseDetailModuleRouter',views.AdCoureseDetailModuleViewModelViewSet)#8.添加课程详情
router.register(r'deleteCoureseDetailModuleRouter',views.DeleteCoureseDetailModuleViewModelViewSet)#9.添加课程详情
router.register(r'contentTypeForModuleViewModelViewSetRouter',views.ContentTypeForModuleViewModelViewSet)#10.获取课程详情(模块、部分)text,image
router.register(r'contentTypeRouter',views.ContentTypeViewModelViewSet)#11.获取课程详情(模块、部分)text,image

urlpatterns = [
       # url(r'^subjects/$',views.SubjectListView.as_view(),name='subject_list'),
       # url(r'^subjects/(?P<pk>\d+)/$',views.SubjectDetailView.as_view(),name='subject_detail'),
       # url(r'^courses/$',views.CourseListView.as_view(), name='course_list'),
       # url(r'^courses/$', views.CourseDetailView.as_view(), name='course_detail'),

       url(r'^',include(router.urls)),#路由api
       url(r'^subjectlist/$',views.subject_list,name='subject_list'),
       url(r'^subjectlist_api/$', views.subject_list_api, name='subject_list'),
       url(r'^subjectAPIView/$',views.SubjectListAPIView.as_view()),
       url(r'^subjectMixins/$', views.SubjectMixins.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)