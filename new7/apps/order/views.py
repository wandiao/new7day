# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers

class OrderViewSet(viewsets.ModelViewSet):
  """
    订单接口
  """
  queryset = models.Order.objects.all()
  serializer_class = common_serializers.OrderSerializer

