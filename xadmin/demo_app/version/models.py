#_**_encoding:utf-8_**_
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 版本更新
class Version(models.Model):
    version = models.CharField(max_length=255,verbose_name=u'版本号')
    content = models.TextField(max_length=5555,verbose_name=u'更新内容')
    url = models.URLField(max_length=255,verbose_name=u'下载网址')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name=u'更新时间')

    class Meta:
        verbose_name = u'版本'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{}.{}'.format(self.version,self.addtime)
