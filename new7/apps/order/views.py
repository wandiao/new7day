# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route
from django.db.transaction import atomic
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
  # schema = auto_schema([
  #   DocParam('invoice', description='票号', location='form',required=True),
  #   DocParam('order_unique', description='流水号', location='form',required=True),
  #   DocParam('order_goods', description='编码', location='form', required=True, type='array'),
  # ])

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
    goods_info = serializer.validated_data['goods_info']
    data = serializer.save()
    for goods in goods_info:
      data = dict(
        goods=goods['goods_id'],
        count=goods['count'],
        order=data.id
      )
      instance = models.Goods.objects.get(pk=goods['goods_id'])
      stock = instance.stock + goods['count']
      goods_serializer = common_serializers.GoodsSerializer(instance, data={
        'stock': stock
      })
      goods_serializer.is_valid(raise_exception=True)
      goods_serializer.save()
      order_goods = common_serializers.OrderGoodsSerializer(data=data)
      order_goods.is_valid(raise_exception=True)
      order_goods.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

    