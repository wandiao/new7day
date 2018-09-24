# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers

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

