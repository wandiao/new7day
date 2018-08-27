# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers

class GoodsViewSet(viewsets.ModelViewSet):
  """
    商品接口
  """
  queryset = models.Goods.objects.all()
  serializer_class = common_serializers.GoodsSerializer

