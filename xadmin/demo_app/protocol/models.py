#_**_encoding:utf-8_**_

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Protocol(models.Model):
    content = models.TextField(max_length=2555,verbose_name=u'协议内容')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'协议'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.content


