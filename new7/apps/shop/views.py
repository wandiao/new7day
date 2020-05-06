# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import datetime
import xlwt
import xlrd
from new7 import models
from new7.common import serializers as common_serializers
from django.db.models import Sum, Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from new7.common.utils import attachment_response
from django.http import HttpResponse
from django.db.transaction import atomic
from rest_framework import (
    viewsets,
    status,
    serializers as rest_serializers
)

from rest_framework.decorators import list_route, detail_route, schema

from . import filters
from . import resources

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

  month_use_export:
  店面使用统计
  """
  queryset = models.Shop.objects.all()
  serializer_class = common_serializers.ShopSerializer
  search_fields = ('name',)
  resource_class = resources.ShopCostResource
  filter_class = filters.ShopFilterSet
  ordering = ('-create_time',)

  @swagger_auto_schema(method='get', manual_parameters=[
    openapi.Parameter('shop', openapi.IN_QUERY, description="店面", type=openapi.TYPE_STRING),
    openapi.Parameter('month', openapi.IN_QUERY, description="月份", type=openapi.TYPE_STRING),
    openapi.Parameter('search', openapi.IN_QUERY, description="商品名、商品简称", type=openapi.TYPE_STRING),
  ])
  @list_route(methods=['get'])
  def month_use_export(self, request, *args, **kwargs):
    shop = self.request.GET.get('shop', None)
    month = self.request.GET.get('month', None)
    search = self.request.GET.get('search', None)
    year = datetime.datetime.now().year
    if month == None:
      month = datetime.datetime.now().month
    queryset = models.GoodsRecord.objects.exclude(shop__isnull=True).filter(record_type='depot_out', record_time__month=month)
    if shop:
      queryset = queryset.filter(shop=shop)
    if search:
      queryset = queryset.filter(Q(goods__name__icontains=search)|Q(goods__short_name__icontains=search))
    queryset = queryset.order_by('shop').values('goods', 'goods__name', 'shop', 'shop__name').annotate(count = Sum('count'), amount=Sum('amount'))
    last_month = 1 if int(month) == 1 else int(month) - 1
    for record in queryset:
      inventory = models.ShopInventory.objects.filter(month=month, goods=record['goods'], shop=record['shop']).first()
      last_inventory = models.ShopInventory.objects.filter(month=last_month, goods=record['goods'], shop=record['shop']).first()
      if not last_inventory:
        class tmp:
          pass
        last_inventory = tmp()
        last_inventory.stock = 0
        last_inventory.amount = 0
      if inventory:
        record['count'] = record['count'] - inventory.stock + (last_inventory.stock or 0)
        record['amount'] = record['amount'] - inventory.amount + (last_inventory.amount or 0)
    response = HttpResponse(content_type='application/ms-excel')
    filename = datetime.datetime.now().strftime('%Y%m%d%H%M') + '.xls'
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = [u'店面名称', u'商品名称', u'商品数量', u'商品成本']
    values = [u'shop__name', u'goods__name', u'count', u'amount']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    for row in queryset:
        row_num += 1
        for col_num in range(len(values)):
            ws.write(row_num, col_num, row[values[col_num]], font_style)

    wb.save(response)
    return response
    

    

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
  ordering = ('-create_time',)

  def create(self, request):
    operator = self.request.user.profile
    request.data['operator'] = operator.id
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    instance = self.perform_create(serializer)
    return Response(serializer.data)

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

class ShopInventoryViewSet(viewsets.ModelViewSet):
  """
  店面盘点接口

  retrieve:
  店面盘点详情

  list:
  店面盘点列表

  create:
  新增店面盘点

  partial_update:
  修改店面盘点

  update:
  修改店面盘点

  delete:
  删除店面盘点

  stats:
  店面盘点统计

  file_import:
  盘点导入
  """
  
  queryset = models.ShopInventory.objects.all()
  serializer_class = common_serializers.ShopInventorySerializer
  filter_class = filters.ShopInventoryFilterSet
  search_fields = ('goods__name','goods__short_name')
  ordering = ('-create_time',)

  def get_serializer_class(self):
    if self.action == 'file_import':
      return common_serializers.FileImportExportSerializer
    return common_serializers.ShopInventorySerializer

  def create(self, request):
    operator = self.request.user.profile
    request.data['operator'] = operator.id
    instance = self.queryset.filter(shop=request.data['shop'], goods=request.data['goods'], month=request.data['month']).first()
    if instance:
      serializer = self.get_serializer(instance, data=request.data, partial=True)
      serializer.is_valid(raise_exception=True)
      serializer.save()
    else:
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      instance = self.perform_create(serializer)
    return Response(serializer.data)

  @swagger_auto_schema(method='get', manual_parameters=[
    openapi.Parameter('shop', openapi.IN_QUERY, description="店面", type=openapi.TYPE_STRING),
  ])
  @list_route(methods=['get'])
  def stats(self, request, *args, **kwargs):
    queryset = models.ShopInventory.objects.all()
    shop = self.request.GET.get('shop', '')
    if shop:
      queryset = queryset.filter(shop=shop)
    
    inventorys = queryset.values('shop', 'shop__name').annotate(total_stock = Sum('stock'), total_amount=Sum('amount'))
    serializer = common_serializers.ShopInventoryStatSerializer(inventorys, many=True)
    return Response(serializer.data)

  @list_route(methods=['post'])  # noqa
  @atomic
  def file_import(self, request, *args, **kwargs):
    operator = self.request.user.profile
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    file = serializer.validated_data['file']
    reader = xlrd.open_workbook(file_contents=file.read(), encoding_override = 'utf8')
    sheet=reader.sheet_by_index(0)
    nrows = sheet.nrows
    for i in range(1, nrows):
      row = sheet.row_values(i)
      shop = models.Shop.objects.get(name=row[0])
      if shop == None:
        raise rest_serializers.ValidationError({
          'error': u'店面%s不存在' % row[0],
        })
      
      goods = models.Goods.objects.get(name=row[1])
      if goods == None:
        raise rest_serializers.ValidationError({
          'error': u'商品%s不存在' % row[1],
        })
      data = dict(
        shop=shop.id,
        goods=goods.id,
        stock=row[2],
        month=row[3],
        price=goods.last_price,
        operator=operator.id,
      )
      good_serializer = common_serializers.ShopInventorySerializer(data=data)
      good_serializer.is_valid(raise_exception=True)
      good_serializer.save()
    return Response(u'导入成功', status.HTTP_201_CREATED)

    
    





