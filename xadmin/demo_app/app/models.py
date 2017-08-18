# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

SERVER_STATUS = (
    (0, u"Normal"),
    (1, u"Down"),
    (2, u"No Connect"),
    (3, u"Error"),
)
SERVICE_TYPES = (
    ('moniter', u"Moniter"),
    ('lvs', u"LVS"),
    ('db', u"Database"),
    ('analysis', u"Analysis"),
    ('admin', u"Admin"),
    ('storge', u"Storge"),
    ('web', u"WEB"),
    ('email', u"Email"),
    ('mix', u"Mix"),
)

@python_2_unicode_compatible
class IDC(models.Model):
    name = models.CharField(max_length=64,verbose_name='姓名')
    description = models.TextField(verbose_name='描述')

    contact = models.CharField(max_length=32,verbose_name='联系人')
    telphone = models.CharField(max_length=32,verbose_name='电话')
    address = models.CharField(max_length=128,verbose_name='地址')
    customer_id = models.CharField(max_length=128,verbose_name='消费者id')
    groups = models.ManyToManyField(Group)  # many
    create_time = models.DateField(auto_now=True,verbose_name='创建日期')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"IDC"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Host(models.Model):
    idc = models.ForeignKey(IDC)
    name = models.CharField(max_length=64,verbose_name='姓名')
    nagios_name = models.CharField(u"Nagios Host ID", max_length=64, blank=True,)
    ip = models.GenericIPAddressField(blank=True, null=True,verbose_name='ip地址')
    internal_ip = models.GenericIPAddressField(blank=True, null=True,verbose_name='互联网ip')
    user = models.CharField(max_length=64,verbose_name='用户')
    password = models.CharField(max_length=128,verbose_name='密码')
    ssh_port = models.IntegerField(blank=True, null=True,verbose_name='ssh端口')
    status = models.SmallIntegerField(choices=SERVER_STATUS,verbose_name='状态')

    brand = models.CharField(max_length=64, choices=[(i, i) for i in (u"DELL", u"HP", u"Other")])
    model = models.CharField(max_length=64,verbose_name='模型')
    cpu = models.CharField(max_length=64,verbose_name='cpu')
    core_num = models.SmallIntegerField(choices=[(i * 2, "%s Cores" % (i * 2)) for i in range(1, 15)])
    hard_disk = models.IntegerField()
    memory = models.IntegerField()

    system = models.CharField(u"System OS", max_length=32, choices=[(i, i) for i in (u"CentOS", u"FreeBSD", u"Ubuntu")])
    system_version = models.CharField(max_length=32)
    system_arch = models.CharField(max_length=32, choices=[(i, i) for i in (u"x86_64", u"i386")])

    create_time = models.DateField(verbose_name='创建日期')
    guarantee_date = models.DateField()
    service_type = models.CharField(max_length=32, choices=SERVICE_TYPES)
    description = models.TextField()

    administrator = models.ForeignKey(AUTH_USER_MODEL, verbose_name="Admin")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Host主人"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class MaintainLog(models.Model):
    host = models.ForeignKey(Host)
    maintain_type = models.CharField(max_length=32)
    hard_type = models.CharField(max_length=16)
    time = models.DateTimeField()
    operator = models.CharField(max_length=16)
    note = models.TextField()

    def __str__(self):
        return '%s maintain-log [%s] %s %s' % (self.host.name, self.time.strftime('%Y-%m-%d %H:%M:%S'),
                                               self.maintain_type, self.hard_type)

    class Meta:
        verbose_name = u"Maintain Log日志"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class HostGroup(models.Model):

    name = models.CharField(max_length=32)
    description = models.TextField()
    hosts = models.ManyToManyField(
        Host, verbose_name=u'Hosts', blank=True, related_name='groups')

    class Meta:
        verbose_name = u"Host Group 用户组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AccessRecord(models.Model):
    date = models.DateField()
    user_count = models.IntegerField()
    view_count = models.IntegerField()

    class Meta:
        verbose_name = u"Access Record 记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s Access Record" % self.date.strftime('%Y-%m-%d')
