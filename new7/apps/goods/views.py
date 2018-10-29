# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import datetime
from rest_framework import viewsets
from django.db.models import Sum
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from new7 import models
from new7.common import serializers as common_serializers
from new7.common.schema import auto_schema, DocParam
from rest_framework.schemas import AutoSchema
import coreapi
from rest_framework.response import Response
from rest_framework import (
    viewsets,
    mixins,
    status,
    serializers as rest_serializers
)
from rest_framework.decorators import list_route, detail_route, schema

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
  商品成本

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
    goods = sorted(paginator.paginate_queryset(self.filter_queryset(self.queryset.all()), request), key=lambda t: t.stock_status)
    serializer = self.get_serializer(goods, many=True)
    return paginator.get_paginated_response(serializer.data)

  @swagger_auto_schema(method='get', manual_parameters=[
    openapi.Parameter('start_time', openapi.IN_QUERY, description="开始时间(xxxx-xx-xx)", type=openapi.TYPE_STRING),
    openapi.Parameter('end_time', openapi.IN_QUERY, description="结束时间(xxxx-xx-xx)", type=openapi.TYPE_STRING),
    openapi.Parameter('depot', openapi.IN_QUERY, description="库房", type=openapi.TYPE_STRING),
    
  ])
  @list_route(methods=['get'])
  def cost(self, request, *args, **kwargs):
    queryset = models.GoodsRecord.objects.all()
    start_time = self.request.GET.get('start_time', None)
    end_time = self.request.GET.get('end_time', None)
    depot = self.request.GET.get('depot', '')
    end_time = datetime.datetime.strptime(
                end_time, '%Y-%m-%d') if end_time else datetime.datetime.now()
    if start_time:
      start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d')
      queryset = queryset.filter(
        record_time__gte=start_time,
        record_time__lte=end_time,
      )
    else:
      queryset = queryset.filter(
        record_time__lte=end_time,
      )
    if depot:
      queryset = queryset.filter(record_depot=depot)
    records = queryset.values('goods', 'goods__name').annotate(count = Sum('count'), cost=Sum('amount'))
    serializer = self.get_serializer(records, many=True)
    return Response(serializer.data)






class GoodsRecordViewSet(viewsets.ModelViewSet):
  """
  商品记录接口
  """

  queryset = models.GoodsRecord.objects.all()
  serializer_class = common_serializers.GoodsRecordSerializer
  filter_class = filters.GoodsRecordFilterSet

