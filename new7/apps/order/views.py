# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import datetime
from rest_framework import (
  viewsets,
  status,
  serializers as rest_serializers,
  )
from rest_framework.decorators import list_route, detail_route
from django.db.transaction import atomic
from django.db.models import F
from rest_framework.response import Response

from new7 import models
from new7.common import serializers as common_serializers
from new7.common.schema import auto_schema, DocParam

class OrderViewSet(viewsets.ModelViewSet):
  """
  订单接口

  retrieve:
  订单详情

  list:
  订单列表

  create:
  新增订单（不可用）

  partial_update:
  修改订单（不可用）

  update:
  修改订单（不可用）

  new:
  新增订单

  delete:
  删除订单
  """

  queryset = models.Order.objects.all()
  serializer_class = common_serializers.OrderSerializer
  schema = auto_schema([
    DocParam('invoice', description='票号', location='form'),
    DocParam('order_unique', description='流水号', location='form'),
    DocParam('order_goods', description='商品信息列表', location='form', type='array'),
  ])
  ordering = ('-create_time',)

  def get_serializer_class(self):
    if self.action == 'new':
        return common_serializers.OrderCreateSerializer
    else:
        return common_serializers.OrderSerializer

  @list_route(methods=['post'])  # noqa
  @atomic
  def new(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    req_data = serializer.validated_data
    goods_info = req_data['goods_info']
    total_count = 0
    total_price = 0
    for goods in goods_info:
      total_count += goods['count']
      total_price += goods['count']* goods['price']
    req_data['total_count'] = total_count
    req_data['total_price'] = total_price
    operator = self.request.user.profile
    operate_time = datetime.datetime.now()
    order_data = serializer.save()
    total_count = 0
    for goods in goods_info:
      instance = models.Goods.objects.get(pk=goods['goods_id'])
      data = dict(
        goods=goods['goods_id'],
        count=goods['count'],
        price=goods.get('price', 0),
        unit=goods.get('unit', instance.unit),
        spec=goods.get('spec', instance.spec),
        order=order_data.id,
        operate_depot = goods.get('operate_depot', None),
        shop=goods.get('shop', None),
      )
      record_data = dict(
        record_type=req_data.get('order_type', 'depot_in'),
        record_time=operate_time,
        order=order_data.id,
        count=goods['count'],
        goods=goods['goods_id'],
        price=goods.get('price', 0),
        operator_account=operator.phone,
        record_depot=goods.get('operate_depot', None),
        remarks=req_data.get('remarks', ''),
        unit=goods.get('unit', instance.unit),
        spec=goods.get('spec', instance.spec),
        shop=goods.get('shop', None),
      )
      amount = 0
      if req_data['order_type'] == 'depot_in':
        stock = instance.stock + goods['count']
        amount = goods['count'] * goods['price']
      elif req_data['order_type'] == 'depot_out':
        if instance.stock - goods['count'] < 0:
          raise rest_serializers.ValidationError({
            'error': u'%s库存不足' % instance.name,
          })
        tmp_count = goods['count']
        while (tmp_count > 0):
          # 取出含有剩余量的第一条数据
          current = models.GoodsRecord.objects.filter(
            record_type='depot_in',
            goods = goods['goods_id'],
            count__gt=F('leave_count'),
            record_depot=goods.get('operate_depot', None),
          ).order_by('record_time').first()
          if current:
            spare = current.count - current.leave_count
            if tmp_count <= spare:
              current.leave_count = current.leave_count + tmp_count
              current.save()
              amount += current.price * tmp_count
              tmp_count = 0
            else:
              current.leave_count = current.count
              current.save()
              amount += current.price * spare
              tmp_count = tmp_count - spare
          else:
            raise rest_serializers.ValidationError({
              'error': u'%s库存不足' % instance.name,
            })  
        stock = instance.stock - goods['count']
      record_data['amount'] = amount
      goods_record = common_serializers.GoodsRecordSerializer(data=record_data)
      goods_record.is_valid(raise_exception=True)
      goods_record.save()
      goods_serializer = common_serializers.GoodsSerializer(instance, data={
        'stock': stock,
        'last_operator': operator.id,
        'last_operate_time': operate_time,
        'last_operate_type': req_data.get('order_type', 'depot_in'),
        'last_price': goods.get('price', 0),
      })
      goods_serializer.is_valid(raise_exception=True)
      goods_serializer.save()
      order_goods = common_serializers.OrderGoodsSerializer(data=data)
      order_goods.is_valid(raise_exception=True)
      order_goods.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

    