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

  retrieve:
  商品详情

  list:
  商品列表

  create:
  新增商品

  partial_update:
  修改商品

  update:
  修改商品

  delete:
  删除商品
  """
  queryset = models.Goods.objects.all()
  serializer_class = common_serializers.GoodsSerializer
  search_fields = ('name', 'short_name')
  filter_class = filters.GoodsFilterSet
  # schema = auto_schema([
  #   DocParam('name', description='名称'),
  #   DocParam('short_name', description='简称'),
  #   DocParam('code', description='编码'),
  #   DocParam('spec', description='规格'),
  # ])
