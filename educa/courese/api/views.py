# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 1.django框架
from django.http  import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 2.rest_framework框架
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.decorators import detail_route,list_route
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# 3.序列器
from .serializers import *
from courese.models import *

# import students.views

# 本项目
from students.models import *
from students.serializers import *

@csrf_exempt
def subject_list(request):

    if request.method == 'GET':
        print ('get')
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects,many=True)
        # serializer.data 将subject实例对象转成python基本数据类型
        return JsonResponse(serializer.data,safe=False)#将Python基本数据类型转成jeson

    elif    request.method == 'POST':
        data = JSONParser().parse(request)
        print (data['title'])
        serializer= SubjectSerializer(data)
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


# 跟iOS客户端通信成功POST
@api_view(['GET','POST'])
def subject_list_api(request):

    if  request.method == 'GET':
        queryset = Subject.objects.all()
        serializer = SubjectSerializer(queryset,many=True)
        return Response(serializer.data)

    elif    request.method == 'POST':
        print ('post')
        # 1.返回单个数据
        # 将传进来的数据通过jeson序列化器序列化
        # serializer = SubjectSerializer(data=request.POST)
        # if  serializer.is_valid():
        #     # serializer.save()#保存到数据库
        #     jesonDic = {'list':[serializer.data],'result':'SUCCESS','errorMessage':''}
        #     return Response(jesonDic)
        #     # return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response({'list':[],'result':'FAILE','errorMessage':'查询错误'})#无效返回错误信息

            # # 2.返回所有数据
        serializer = SubjectSerializer(data=request.POST)#将客户端传进来的参数序列化成模型
        if serializer.is_valid():#判断序列化有效,返回正确信息
            # print (serializerData.data['title'])
            # serializer.data取出序列化器里面的字典数据,放进数组里面
            queryset = Subject.objects.all()#从数据库获取所有模型
            serializer = SubjectSerializer(queryset, many=True)#将所有模型数据序列化
            jesonDic = {'list':serializer.data,'result':'SUCCESS','errorMessage':'查询成功'}
            return Response(jesonDic) #将jeson数据返回给客户端
        else:
            print ('无效')
            return Response({'list':[],'result':'FAILE','errorMessage':'参数错误'})#无效返回错误信息
            # return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


# APIView视图
class   SubjectListAPIView(APIView):

    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)#阻止默认用户访问视图
    def get(self,request,format=None):
        print ('哈哈get')
        serializers = SubjectSerializer(data=request.data,many=True)#接收客户端传进来的参数并且实例化
        if  serializers.is_valid():#判断数据有效,有效返回正确信息,所有列表数据
            # queryset = Subject.objects.all()  # 从数据库获取所有模型
            subjects = Subject.objects.all()
            serializer = SubjectSerializer(subjects, many=True)  # 将所有模型数据序列化
            jesonDic = {'list': serializer.data, 'result': 'SUCCESS', 'errorMessage': '查询成功'}
            return Response(jesonDic)#返回jeson
        jesonDic = {'list': [], 'result': 'SUCCESS', 'errorMessage': '参数验证失败'}#失败
        return Response(jesonDic)#返回jeson
        # return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,format=None):
        print ('post')
        print (request.POST)
        print (request.POST['title'])#接收客户端传过来的title,打印值,判断值是否为空,为空提示错误
        # serializers = SubjectSerializer(data=request.POST)#接收客户端传进来的参数并实例化
        if  request.POST['title'] is not None:#判断数据有效,有效返回正确信息
            # print (serializers.data)
            # serializer.save()#保存到数据库
            subjects = Subject.objects.all()
            serializers = SubjectSerializer(subjects,many=True)
            # return Response(serializers.data,status=status.HTTP_201_CREATED)
            jesonDic = {'list': serializers.data, 'result': 'SUCCESS', 'errorMessage': '查询成功'}
            return Response(jesonDic)  # 返回jeson
        jesonDic = {'list': [], 'result': 'FAILE', 'errorMessage': '参数验证失败'}
        return Response(jesonDic)
        # return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class   SubjectMixins(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # get请求
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    #post请求
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


# viewsets 只读
class   SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



# 我在 ModelViewSet 中自定义了方法 plaintext，rest_framework 中对于自定义的 viewset 方法提供了两种装饰器
#
#     list_route
#     detail_route
#
# 区别就是 list_route 的参数不包含 pk（对应 list），而 detail_route 包含pk（对应 retrieve）
#
# 看一段代码就懂了
#
# @list_route(methods=['post', 'delete'])
# def custom_handler(self, request):
#     pass
#
#
# @detail_route(methods=['get'])
# def custom_handler(self, request, pk=None):
#     pass


# 2.科目列表ModelViewSet
class   SubjectViewModelViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    print ('get --- SubjectViewModelViewSet')
    # @detail_route(methods=['post'],authentication_classes=(BasicAuthentication,),permission_classes = (IsAuthenticated,))
    @list_route(methods=['post'],)
    def enroll(self, request, *args, **kwargs):
        print ('post')
        print (request.POST)
        print (request.POST['title'])  # 接收客户端传过来的title,打印值,判断值是否为空,为空提示错误
        title = request.POST['title']
        if  title is not None:
            subjects = Subject.objects.all().order_by('id')[:10]#按id排序,取前10个数据
            serializer = self.get_serializer(subjects, many=True)#获取到序列化器,将subjects对象序列化
            jesonDic = {'list': serializer.data, 'result': 'SUCCESS', 'errorMessage': '查询成功'}
            return Response(jesonDic)  # 返回jeson
        jesonDic = {'list': [], 'result': 'FAILE', 'errorMessage': '参数错误'}
        return Response(jesonDic)  # 返回jeson


# #  @detail_route(methods=['post'])
#     def set_password(self, request, pk=None):
#         user = self.get_object()
#         serializer = PasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user.set_password(serializer.data['password'])
#             user.save()
#             return Response({'status': 'password set'})
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#
#     @list_route()
#     def recent_users(self, request):
#         recent_users = User.objects.all().order('-last_login')
#
#         page = self.paginate_queryset(recent_users)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(recent_users, many=True)
#         return Response(serializer.data)

# 3.课程列表
class   CourseViewModelViewSet(viewsets.ModelViewSet):
        queryset = Course.objects.all()
        serializer_class = CourseSerializer
        @list_route(methods=['post'],)
        def courselist(self,request,*args,**kwargs):
            subject_id = request.POST['id']#获取传过来的科目id
            if  subject_id  is  not None:
                course = Course.objects.filter(subject_id = subject_id)
                serializer_course = self.get_serializer(course,many=True)
                jesonDic = {'list':serializer_course.data,'result': 'SUCCESS', 'errorMessage': '查询成功'}
                # jesonDic = {'list': [], 'result': 'SUCCESS', 'errorMessage': '参数错误'}
                return Response(jesonDic)
            jesonDic = {'list': [], 'result': 'FAILE', 'errorMessage': '参数错误'}
            return Response(jesonDic)


# 4.课程详情
class CoureseDetailViewModelRouter(viewsets.ModelViewSet):
        queryset = Module.objects.all()#模块
        serializer_class = ModuleSerializer

        @list_route(methods=['post'],)
        def coureseDetail(self,request,*args,**kwargs):
            course_id = request.POST['id']
            if  course_id  is not  None:
                module_list = Module.objects.all().filter(course_id=course_id)
                serializer_module = self.get_serializer(module_list,many=True)
                jesonDic = {'list':serializer_module.data,'result': 'SUCCESS', 'errorMessage': '查询成功'}
                return Response(jesonDic)
            jesonDic = {'list': [], 'result': 'FAILE', 'errorMessage': '参数错误'}
            return Response(jesonDic)

# 5.注册
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


# 6.登录
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


#7.更新课程详情
class   UpdateCoureseDetailModuleViewModelViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    @list_route(methods=['post'])
    def courseModuleUpdate(self,request,*args,**kwargs):
        print (request.POST['description'])
        if request.POST['description'] is None:
            return Response({'list':[],'result': 'FAILE', 'errorMessage': '内容不能为空'})

        # course_id=和course_id__exact=等价
        # id 和 pk等价
        # get获取单一对象。必须保证数据库有这条数据,否则异常
        module = Module.objects.all().get(pk=request.POST['id'],course_id__exact=request.POST['courseId'])
        # module_arr = Module.objects.all().filter(id=request.POST['id'],course_id__exact=request.POST['courseId'])

        if  module is not None:
            # modul = module_arr.first()
            # 如果用filter获取数据,那么必须定义modul接收,否则下面的属性字段保存不到数据库
            module.description = request.POST['description']
            module.save()#保存对数据库中已存在的对象的改动,相当于update
            module_serializer = ModuleSerializer(module) #序列化单个对象,返回的data是字典,不是数组.因为上面获取的是单一对象
            return Response({'list':module_serializer.data,'result': 'SUCCESS', 'errorMessage': '更新成功'})


# 8.增加课程详情
class   AdCoureseDetailModuleViewModelViewSet(viewsets.ModelViewSet):
    # description
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    @list_route(methods=['post'])
    def courseModuleAdd(self,request,*args,**kwargs):
        if request.POST['description']  is None:
            return Response({'list':[],'result': 'FAILE', 'errorMessage': '内容不能为空'})

        if request.POST['title'] is None:
            return Response({'list': [], 'result': 'FAILE', 'errorMessage': '标题不能为空'})

        module = Module(title=request.POST['title'],description=request.POST['description'],
                            course_id=request.POST['courseId'],
                            )
        if module is not None:
            module.save()
            module_serializer = ModuleSerializer(module) #序列化单个对象,返回的data是字典,不是数组.因为上面获取的是单一对象
            return Response({'list': module_serializer.data, 'result': 'SUCCESS', 'errorMessage': '添加成功'})
        return Response({'list': [], 'result': 'FAILE', 'errorMessage': '添加失败'})

# 9.删除课程详情
class   DeleteCoureseDetailModuleViewModelViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    @list_route(methods=['post'])
    def courseModuleDelete(self,request,*args,**kwargs):
        module = Module.objects.all().get(pk=request.POST['id'],course_id__exact=request.POST['courseId'])
        if  module  is not None: #判断模型(数据库取出来的)是否存在
            module.delete()
            return Response({'list': [], 'result': 'SUCCESS', 'errorMessage': '删除成功'})
        return Response({'list': [], 'result': 'FAILE', 'errorMessage': '删除失败'})



# 10.获取课程详情(模块、部分)下面的内容 -- text、file、url、video
class   ContentTypeForModuleViewModelViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    @list_route(methods=['post'])
    def contentTypeList(self,request,*args,**kwargs):
        if request.POST['id'] is None:
            return Response({'list': [], 'result': 'FAILE', 'errorMessage': '参数错误'})
        content_arr = Content.objects.all().filter(module_id__exact=request.POST['id'])
        for objc in  content_arr:
            print ('内容类型:' + str(objc.content_type) + '\n' + '内容类型id:' + str(objc.content_type_id) + '\n')
        if len(content_arr) == 0:
            return Response({'list': [], 'result': 'SUCCESS', 'errorMessage': '暂无数据'})
        serializer_content = self.get_serializer(content_arr,many=True)
        return Response({'list': serializer_content.data, 'result': 'SUCCESS', 'errorMessage': '查询成功'})



# 11.获取具体内容text,image
class ContentTypeViewModelViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    @list_route(methods=['post'])#必须声明post,get
    def typelist(self, request, *args, **kwargs):
        if request.POST['id'] is None:
            return Response({'list': [], 'result': 'FAILE', 'errorMessage': '参数错误'})
        #  get_for_id(id)返回表示该模型的ContentType 实例
        #  get_for_model 接收一个模型类或模型的实例，并返回表示该模型的ContentType 实例
        content_type = ContentType.objects.get_for_id(id=request.POST['id'])#1.先获取内容类型(Text,Image)
        print ('11内容类型:' + str(content_type) + '\n' + '11内容类型id:' + str(request.POST['objectId']) + '\n')
        # content_type.model_class() <class 'courese.models.Text'>#2.返回类型Text
        # content_type.get_object_for_this_type(id=4)#3.返回类型Text中id=4的具体数据内容
        # content_type.get_all_objects_for_this_type()4.返回类型Text中所有数据内容
        # # 2.根据内容类型id:content_type.id,object_id__exact=获取具体内容
        # content_arr = Content.objects.filter(content_type_id__exact=content_type.id,
        #                                      object_id__exact=request.POST['objectId'])
        # get_object_for_this_type() 和model_class() 一起使用可以实现两个极其重要的功能︰
        # 3.在这里判断content_type的类型,然后再获取所有数据
        if  content_type.model_class() == Text:#Text
            text_arr = content_type.get_all_objects_for_this_type()
            if len(text_arr) == 0:
                return Response({'list': [], 'result': 'SUCCESS', 'errorMessage': '暂无数据'})
            text_serializer = TextSerializer(text_arr,many=True)
            return Response({'list': text_serializer.data, 'result': 'SUCCESS', 'errorMessage': '查询成功'})
        elif content_type.model_class() ==  Video:#Video
            video_arr = content_type.get_all_objects_for_this_type()
            if len(video_arr) == 0:
                return Response({'list': [], 'result': 'SUCCESS', 'errorMessage': '暂无数据'})
            video_serializer = VideoSerializer(video_arr,many=True)
            return Response({'list': video_serializer.data, 'result': 'SUCCESS', 'errorMessage': '查询成功'})
        elif content_type.model_class() == File:#File
            file_arr = content_type.get_all_objects_for_this_type()
            if len(file_arr) == 0:
                return Response({'list': [], 'result': 'SUCCESS', 'errorMessage': '暂无数据'})
            file_serializer = VideoSerializer(file_arr, many=True)
            return Response({'list': file_serializer.data, 'result': 'SUCCESS', 'errorMessage': '查询成功'})
        elif content_type.model_class() == Image:#Image
            image_arr = content_type.get_all_objects_for_this_type()
            if len(image_arr) == 0:
                return Response({'list': [], 'result': 'SUCCESS', 'errorMessage': '暂无数据'})
            image_serializer = ImageSerializer(image_arr, many=True)
            return Response({'list': image_serializer.data, 'result': 'SUCCESS', 'errorMessage': '查询成功'})




