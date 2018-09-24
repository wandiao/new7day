# coding:utf-8

from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRelation,
)

from django.db import models

from .base import (
    BaseModel,
    DeletedMixin,
)

class Profile(DeletedMixin, BaseModel):
  ROLE_CHOICES = (
    ('super_admin', u'超级管理员'),
    ('admin', u'管理员'),
    ('worker', u'业务员'),
    ('warekeeper', u'仓库管理员')
  )
  GENDER = (
    (1, u'男'),
    (2, u'女'),
  )
  content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')
  role = models.CharField(
    u'角色',
    max_length=20,
    choices=ROLE_CHOICES,
    default='worker',
    help_text=u'角色',
  )
  user = models.OneToOneField(
    'auth.User',
    verbose_name=u'用户',
    on_delete=models.PROTECT,
    help_text=u'用户',
  )
  name = models.CharField(
    u'姓名',
    max_length=20,
    help_text=u'姓名'
  )
  gender = models.IntegerField(
    u'性别',
    choices=GENDER,
    default=1,
    help_text=u'性别',
  )

  birth = models.DateTimeField(
      u'出生日期',
      blank=True,
      null=True,
      help_text=u'出生日期',
  )

  code = models.CharField(
    u'员工编号',
    max_length=200,
    unique=True,
    null=True,
    help_text=u'员工编号',
  )

  phone = models.CharField(
    u'电话',
    max_length=20,
    help_text=u'电话',
  )
  phone_verified = models.BooleanField(
    u'电话是否已验证',
    default=False,
    blank=True,
    help_text=u'电话是否已验证',
  )
  address = models.CharField(
    u'地址',
    max_length=20,
    blank=True,
    null=True,
    help_text=u'地址'
  )
  salary = models.IntegerField(
    u'工资',
    default=0,
    help_text=u'工资'
  )
  desc = models.CharField(
      u'描述',
      max_length=100,
      null=True,
      blank=True,
      help_text=u'描述',
  )
  depot = models.ForeignKey(
    'new7.Depot',
    verbose_name=u'负责仓库',
    blank=True,
    null=True,
    related_name='depot_keepers',
    on_delete=models.PROTECT,
    help_text=u'负责仓库',
  )

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = u'个人信息'
    verbose_name_plural = verbose_name
