# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import datetime
import xlrd
from django.db.transaction import atomic
from rest_framework import viewsets
from django.db.models import Sum, F
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from collections import OrderedDict

from new7 import models
from new7.common import serializers as common_serializers
from new7.common.schema import auto_schema, DocParam
from rest_framework.schemas import AutoSchema
from django.core.mail import send_mail
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

  stats:
  成本月度统计

  file_import:
  商品导入

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
    elif self.action == 'stats':
      return common_serializers.GoodsStatsSerializer
    elif self.action == 'file_import':
      return common_serializers.FileImportExportSerializer
    return common_serializers.GoodsSerializer

  @list_route(methods=['get'])
  def stock(self, request, *args, **kwargs):
    depot = request.GET.get('depot', None)
    stock_status = request.GET.get('stock_status', '')
    pagination_class = Pagination
    paginator = pagination_class()
    goods_list = paginator.paginate_queryset(self.filter_queryset(self.queryset.order_by('stock_status').all()), request)
    for goods in goods_list:
      if depot:
        current_depot_stock = models.GoodsRecord.objects.filter(
          record_depot=depot,
          record_type='depot_in',
          goods=goods.id,
        ).aggregate(current_count = Sum('count'), current_leave_count = Sum('leave_count'))
      else:
        current_depot_stock = models.GoodsRecord.objects.filter(
          record_type='depot_in',
          goods=goods.id,
        ).aggregate(current_count = Sum('count'), current_leave_count = Sum('leave_count'))
      if current_depot_stock['current_count'] != None:
        current_count = current_depot_stock['current_count'] - current_depot_stock['current_leave_count']
        print(current_count)
      else:
        current_count = 0
      
      goods.current_depot_stock = current_count
    serializer = self.get_serializer(goods_list, many=True)
    return paginator.get_paginated_response(serializer.data)

  @swagger_auto_schema(method='get', manual_parameters=[
    openapi.Parameter('start_time', openapi.IN_QUERY, description="开始时间(xxxx-xx-xx)", type=openapi.TYPE_STRING),
    openapi.Parameter('end_time', openapi.IN_QUERY, description="结束时间(xxxx-xx-xx)", type=openapi.TYPE_STRING),
    openapi.Parameter('depot', openapi.IN_QUERY, description="库房", type=openapi.TYPE_STRING),
    openapi.Parameter('shop', openapi.IN_QUERY, description="店面", type=openapi.TYPE_STRING),
  ])
  @list_route(methods=['get'])
  def cost(self, request, *args, **kwargs):
    queryset = models.GoodsRecord.objects.all()
    start_time = self.request.GET.get('start_time', None)
    end_time = self.request.GET.get('end_time', None)
    damaged_queryset = models.GoodsDamaged.objects.all()
    depot = self.request.GET.get('depot', '')
    shop = self.request.GET.get('shop', '')
    page = int(self.request.GET.get('page', 1))
    page_size = int(self.request.GET.get('page_size', 50))
    end_time = datetime.datetime.strptime(
                end_time, '%Y-%m-%d') if end_time else datetime.datetime.now()
    if start_time:
      start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d')
      queryset = queryset.filter(
        record_time__gte=start_time,
        record_time__lte=end_time,
      )
      damaged_queryset = damaged_queryset.filter(
        report_time__gte=start_time,
        report_time__lte=end_time,
      )
    else:
      queryset = queryset.filter(
        record_time__lte=end_time,
      )
      damaged_queryset = damaged_queryset.filter(
        report_time__lte=end_time,
      )
    if depot:
      queryset = queryset.filter(record_depot=depot)
    if shop:
      queryset = queryset.filter(shop=shop)
    records = queryset.filter(record_type='depot_in').values('goods', 'goods__name', 'unit', 'spec').annotate(count = Sum('count'), cost=Sum('amount'))
    for record in records:
      out_record = queryset.filter(record_type='depot_out', goods=record['goods']).aggregate(used_count = Sum('count'), used_cost=Sum('amount'))
      damaged_record = damaged_queryset.filter(goods=record['goods']).aggregate(damaged_count = Sum('count'), damaged_cost=Sum('amount'))
      record['used_count'] = out_record['used_count']
      record['used_cost'] = out_record['used_cost']
      record['damaged_count'] = damaged_record['damaged_count']
      record['damaged_cost'] = damaged_record['damaged_cost']
    serializer = self.get_serializer(records[(page - 1)*page_size:page*page_size], many=True)
    return Response(OrderedDict([
      ('count', records.count()),
      ('page_size', page_size),
      ('total_page', int((records.count() + page_size - 1)/page_size)),
      ('current_page', page),
      ('resluts', serializer.data)
    ]))
  
  @swagger_auto_schema(method='get', manual_parameters=[
    openapi.Parameter('depot', openapi.IN_QUERY, description="仓库", type=openapi.TYPE_STRING),
    openapi.Parameter('shop', openapi.IN_QUERY, description="店面", type=openapi.TYPE_STRING),
    openapi.Parameter('goods_id', openapi.IN_QUERY, description="商品id", type=openapi.TYPE_STRING),
  ])
  @list_route(methods=['get'])
  def stats(self, request, *args, **kwargs):
    depot = self.request.GET.get('depot', None)
    shop = self.request.GET.get('shop', None)
    goods_id = self.request.GET.get('goods_id', None)
    queryset = models.GoodsRecord.objects.all()
    damaged_queryset = models.GoodsDamaged.objects.all()
    if depot:
      queryset = queryset.filter(record_depot=depot)
      damaged_queryset = damaged_queryset.filter(damaged_depot=depot)
    if shop:
      queryset = queryset.filter(shop=shop)
      damaged_queryset = damaged_queryset.filter(damaged_shop=shop)
    if goods_id:
      queryset = queryset.filter(goods=goods_id)
    res = []
    for n in range (1, 13):
      current = queryset.filter(
        record_time__month=n,
        record_type='depot_in',
      ).aggregate(count = Sum('count'), cost=Sum('amount'))
      print(current)
      used_current = queryset.filter(
        record_time__month=n,
        record_type='depot_out',
      ).aggregate(used_count = Sum('count'), used_cost=Sum('amount'))
      damaged_current = damaged_queryset.filter(
        report_time__month=n,
      ).aggregate(damaged_count = Sum('count'), damaged_cost=Sum('amount'))
      month_data = dict(
        month=n,
        count=current.get('count', 0),
        cost=current.get('cost', 0),
        used_count=used_current.get('used_count', 0),
        used_cost=used_current.get('used_cost', 0),
        damaged_count=damaged_current.get('damaged_count', 0),
        damaged_cost=damaged_current.get('damaged_cost', 0),
      )
      res.append(month_data)
    stats_data = self.get_serializer(res, many=True)
    return Response(stats_data.data)

  @list_route(methods=['post'])  # noqa
  @atomic
  def file_import(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    operator = self.request.user.profile
    serializer.is_valid(raise_exception=True)
    file = serializer.validated_data['file']
    reader = xlrd.open_workbook(file_contents=file.read(), encoding_override = 'utf8')
    sheet=reader.sheet_by_index(0)
    nrows = sheet.nrows
    for i in range(1, nrows):
      row = sheet.row_values(i)
      data = dict(
        name=row[0],
        short_name=row[1],
        code=row[2],
        in_price=row[3],
        sale_price=row[4],
        spec=row[5],
        unit=row[6],
        warn_stock=row[7],
        desc=row[8],
      )
      if models.Goods.objects.filter(name=row[0]):
        raise rest_serializers.ValidationError({
          'error': u'商品%s已存在' % row[0],
        })
      good_serializer = common_serializers.GoodsSerializer(data=data)
      good_serializer.is_valid(raise_exception=True)
      good_serializer.save()
    return Response(u'导入成功', status.HTTP_201_CREATED)


    










class GoodsRecordViewSet(viewsets.ModelViewSet):
  """
  商品记录接口
  """

  queryset = models.GoodsRecord.objects.all()
  serializer_class = common_serializers.GoodsRecordSerializer
  filter_class = filters.GoodsRecordFilterSet
  search_fields = ('goods__name',)
  ordering = ('-record_time',)


class GoodsDamagedViewSet(viewsets.ModelViewSet):
  """
  商品报损接口

  retrieve:
  报损详情

  list:
  报损列表

  create:
  新增报损

  partial_update:
  修改报损

  update:
  修改报损

  delete:
  删除报损
  """

  

  queryset = models.GoodsDamaged.objects.all()
  serializer_class = common_serializers.GoodsDamagedSerializer
  filter_class = filters.GoodsDamagedFilterSet
  ordering = ('-report_time',)

  def create(self, request):
    data = request.data
    operate_time = datetime.datetime.now()
    operator = self.request.user.profile
    data['amount'] = data['price'] * data['count']
    data['operator'] = operator.id
    data['report_time'] = operate_time
    instance = models.Goods.objects.get(pk=data['goods'])
    if 'damaged_depot' in data:
      if instance.stock - data['count'] < 0:
        raise rest_serializers.ValidationError({
          'error': '报损数量超过库存数',
        })
      tmp_count = data['count']
      while (tmp_count > 0):
        # 取出含有剩余量的第一条数据
        current = models.GoodsRecord.objects.filter(
          record_type='depot_in',
          goods = data['goods'],
          count__gt=F('leave_count'),
          record_depot=data['damaged_depot'],
        ).order_by('record_time').first()
        if current:
          spare = current.count - current.leave_count
          if tmp_count <= spare:
            current.leave_count = current.leave_count + tmp_count
            current.save()
            tmp_count = 0
          else:
            current.leave_count = current.count
            current.save()
            tmp_count = tmp_count - spare
        else:
          raise rest_serializers.ValidationError({
            'error': '报损数量超过库存数',
          })  
      instance.stock = instance.stock - data['count']
      instance.save()
    
    serializer = common_serializers.GoodsDamagedSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



