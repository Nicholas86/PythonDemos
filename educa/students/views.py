# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from django.shortcuts import render

# Create your views here.

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.http  import HttpResponse,JsonResponse

# rest_fromework
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework import viewsets


# 本项目
from .models import *
from .serializers import *


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super(StudentRegistrationView,
                       self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result

# 1.注册
class  RegisterModelViewSet(viewsets.ModelViewSet):

    queryset = Register.objects.all()
    serializer_class = RegisterSerializers

    @list_route(methods=['post'])
    def register(self,request,pk=None):
        name = request.POST['name']
        # register = Register.objects.get(name=name) 如果数据库没有数据,会抛出DoesNotExist异常。慎用。
        register_queryset = self.queryset.filter(name=name)#获取的结果是个数组

        if (len(register_queryset) != 0): #判断是否注册过,通过数组长度个数
            return Response({'list':[],'result':'FAILE','errorMessage':'该账号已注册'})

        serializer = RegisterSerializers(data=request.POST) #序列化数据
        if serializer.is_valid():
            user = Register(name=request.POST['name'],password=request.POST['password'])
            user.save()
            return Response({'list':[],'result':'SUCCESS','errorMessage':'注册成功'})
        return Response({'list':[],'result':'FAILE','errorMessage':'注册失败'})


# 2.登录
class  LoginModelViewSet(viewsets.ModelViewSet):

        queryset = Register.objects.all()
        serializer_class = RegisterSerializers

        @list_route(methods=['post'])
        def login(self,request,*args,**kwargs):

            register_arr = Register.objects.all().filter(name=request.POST['name'],)#根据用户名,查询到所有数据

            if len(register_arr) == 0:
                return Response({'list': [], 'result': 'FAILE', 'errorMessage': '该账号没有注册,请先注册'})
            # register_arr[0] 获取数组第一个元素
            if register_arr.first().password != request.POST['password']: #判断密码是否相等
                return Response({'list': [], 'result': 'FAILE', 'errorMessage': '密码错误'})

            register_serializer = RegisterSerializers(register_arr,many=True)#jeson

            return Response({'list': register_serializer.data, 'result': 'SUCCESS', 'errorMessage': '登录成功'})






