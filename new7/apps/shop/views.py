# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers

from . import filters

class ShopViewSet(viewsets.ModelViewSet):
  """
  店面接口

  retrieve:
  店面详情

  list:
  店面列表

  create:
  新增店面

  partial_update:
  修改店面

  update:
  修改店面

  delete:
  删除店面
  """
  queryset = models.Shop.objects.all()
  serializer_class = common_serializers.ShopSerializer
  search_fields = ('name',)
  filter_class = filters.ShopFilterSet

