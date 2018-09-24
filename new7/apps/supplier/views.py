# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers
from new7.common.schema import auto_schema, DocParam
from django.http import JsonResponse

from . import filters

class SupplierViewSet(viewsets.ModelViewSet):
  """
  供应商接口

  retrieve:
  供应商详情

  list:
  供应商列表

  create:
  新增供应商

  partial_update:
  修改供应商

  update:
  修改供应商

  delete:
  删除供应商
  """
  queryset = models.Supplier.objects.all()
  serializer_class = common_serializers.SupplierSerializer
  filter_class = filters.SupplierFilterSet
  search_fields = ('name')

  def get(self, request, *args, **kwargs):
        return JsonResponse("Hello world!!!!!!!!++++++中文测试")
  # schema = auto_schema([
  #   DocParam('name', description='名称'),
  #   DocParam('type', description='供应商类型'),
  # ])

