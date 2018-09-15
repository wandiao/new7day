# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers
from new7.common.schema import auto_schema, DocParam

from . import filters

class SupplierViewSet(viewsets.ModelViewSet):
  """
    供应商接口
  """
  queryset = models.Supplier.objects.all()
  serializer_class = common_serializers.SupplierSerializer
  filter_class = filters.SupplierFilterSet
  search_fields = ('name')
  schema = auto_schema([
    DocParam('name', description='名称'),
    DocParam('type', description='供应商类型'),
  ])

