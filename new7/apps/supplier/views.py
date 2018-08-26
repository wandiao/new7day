# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers

class SupplierViewSet(viewsets.ModelViewSet):
  """
    供应商接口
  """
  queryset = models.Supplier.objects.all()
  serializer_class = common_serializers.SupplierSerializer

