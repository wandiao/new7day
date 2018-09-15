# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers
from new7.common.schema import auto_schema, DocParam

from . import filters

class GoodsViewSet(viewsets.ModelViewSet):
  """
    商品接口
  """
  queryset = models.Goods.objects.all()
  serializer_class = common_serializers.GoodsSerializer
  filter_class = filters.GoodsFilterSet
  schema = auto_schema([
    DocParam('name', description='商品名称'),
    DocParam('short_name', description='商品简称'),
    DocParam('code', description='编码'),
    DocParam('spec', description='规格'),
  ])
