# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.db import models
from django.contrib.auth.models import User
from courese.models import *
# Create your models here.
# students_orderCourse

class OrderCourse(models.Model):
    # course_id = models.IntegerField(verbose_name='课程id')
    course = models.ForeignKey(Course,related_name='course',verbose_name='课程')

    class Meta:
        verbose_name = '报名的课程'
        verbose_name_plural = u'报名的课程'

    def __str__(self):
        return str(self.course)

class Register(models.Model):
    name = models.IntegerField(verbose_name='用户名',)
    password = models.CharField(verbose_name='密码',max_length=250)

    class   Meta:
        verbose_name = u'注册'
        verbose_name_plural = u'注册'

    def __str__(self):
        return str(self.name)



