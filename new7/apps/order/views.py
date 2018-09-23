# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from django.db.transaction import atomic
from rest_framework.response import Response

from new7 import models
from new7.common import serializers as common_serializers

class OrderViewSet(viewsets.ModelViewSet):
  """
    订单接口
  """
  queryset = models.Order.objects.all()
  serializer_class = common_serializers.OrderSerializer

  def get_serializer_class(self):
    if self.action == 'new':
        return common_serializers.OrderCreateSerializer
    else:
        return common_serializers.OrderSerializer

  @list_route(methods=['post'])  # noqa
  @atomic
  def new(self, request, *args, **kwargs):
    '''
    新增订单
    '''
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    goods_info = serializer.validated_data['goods_info']
    data = serializer.save()
    for goods in goods_info:
      data = dict(
        goods_id=goods['goods_id'],
        count=goods['count'],
        order_id=data.id
      )
      order_goods = common_serializers.OrderGoodsSerializer(data=data)
      order_goods.is_valid(raise_exception=True)
      order_goods.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

    