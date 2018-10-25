# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from django.db.models import Sum
from new7 import models
from new7.common import serializers as common_serializers
from new7.common.schema import auto_schema, DocParam
from rest_framework.response import Response
from rest_framework import (
    viewsets,
    mixins,
    status,
    serializers as rest_serializers
)
from rest_framework.decorators import list_route, detail_route

from . import filters
from new7.common.pagination import Pagination

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

  stock:
  商品库存

  cost:
  商品库存

  delete:
  删除商品
  """
  queryset = models.Goods.objects.all()
  serializer_class = common_serializers.GoodsSerializer
  search_fields = ('name', 'short_name')
  filter_class = filters.GoodsFilterSet

  def get_serializer_class(self):
    if self.action == 'stock':
      return common_serializers.GoodsStockSerializer
    elif self.action == 'cost':
      return common_serializers.GoodsCostSerializer
    return common_serializers.GoodsSerializer

  @list_route(methods=['get'])
  def stock(self, request, *args, **kwargs):
    pagination_class = Pagination
    paginator = pagination_class()
    goods = paginator.paginate_queryset(self.filter_queryset(self.queryset.all()), request)
    serializer = self.get_serializer(goods, many=True)
    return paginator.get_paginated_response(serializer.data)

  @list_route()
  def cost(self, request, *args, **kwargs):
    records = models.GoodsRecord.objects.values('goods', 'goods__name').annotate(count = Sum('count'), cost=Sum('amount')).all()
    print(records)
    serializer = self.get_serializer(records, many=True)
    return Response(serializer.data)






class GoodsRecordViewSet(viewsets.ModelViewSet):
  """
  商品记录接口
  """

  queryset = models.GoodsRecord.objects.all()
  serializer_class = common_serializers.GoodsRecordSerializer
  filter_class = filters.GoodsRecordFilterSet

