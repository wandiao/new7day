# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers
from new7.common.schema import auto_schema, DocParam

from . import filters

class DepotViewSet(viewsets.ModelViewSet):
  """
  仓库接口

  retrieve:
  仓库详情

  list:
  仓库列表

  create:
  新增仓库

  partial_update:
  修改仓库

  update:
  修改仓库

  delete:
  删除仓库
  """
  queryset = models.Depot.objects.all()
  serializer_class = common_serializers.DepotSerializer
  filter_class = filters.DepotFilterSet
  search_fields = ('name')


