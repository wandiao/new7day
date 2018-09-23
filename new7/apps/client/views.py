# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers

class ClientViewSet(viewsets.ModelViewSet):
  """
  客户接口

  retrieve:
  客户详情

  list:
  客户列表

  create:
  新增客户

  partial_update:
  修改客户

  update:
  修改客户

  delete:
  删除客户
  """
  queryset = models.Client.objects.all()
  serializer_class = common_serializers.ClientSeralizer

