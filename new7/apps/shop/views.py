# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import datetime
from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers
from django.db.models import Sum
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from rest_framework.decorators import list_route, detail_route, schema

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

class ShopIncomeViewSet(viewsets.ModelViewSet):
  """
  店面收入接口

  retrieve:
  店面收入详情

  list:
  店面收入列表

  create:
  新增店面收入

  partial_update:
  修改店面收入

  update:
  修改店面收入

  delete:
  删除店面收入

  stats:
  店面收入统计
  """
  
  queryset = models.ShopIncome.objects.all()
  serializer_class = common_serializers.ShopIncomeSerializer

  @swagger_auto_schema(method='get', manual_parameters=[
    openapi.Parameter('start_time', openapi.IN_QUERY, description="开始时间(xxxx-xx-xx)", type=openapi.TYPE_STRING),
    openapi.Parameter('end_time', openapi.IN_QUERY, description="结束时间(xxxx-xx-xx)", type=openapi.TYPE_STRING),
    openapi.Parameter('shop', openapi.IN_QUERY, description="店面", type=openapi.TYPE_STRING),
  ])
  @list_route(methods=['get'])
  def stats(self, request, *args, **kwargs):
    queryset = models.ShopIncome.objects.all()
    start_time = self.request.GET.get('start_time', None)
    end_time = self.request.GET.get('end_time', None)
    shop = self.request.GET.get('shop', '')
    end_time = datetime.datetime.strptime(
                end_time, '%Y-%m-%d') if end_time else datetime.datetime.now()
    if start_time:
      start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d')
      queryset = queryset.filter(
        create_time__gte=start_time,
        create_time__lte=end_time,
      )
    else:
      queryset = queryset.filter(
        create_time__lte=end_time,
      )
    
    if shop:
      queryset = queryset.filter(shop=shop)
    
    incomes = queryset.values('shop').annotate(income = Sum('income'))
    serializer = self.get_serializer(incomes, many=True)
    return Response(serializer.data)

    
    





