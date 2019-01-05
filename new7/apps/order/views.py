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
from django.http import Http404

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

  def destroy(self, request, pk=None):
    try:
      instance = self.get_object()
      first = models.Order.objects.order_by('-create_time').first()
      if int(pk) != int(first.id):
        raise rest_serializers.ValidationError({
          'error': '该数据无法删除',
        }) 
      order_goods_list = models.OrderGoods.objects.filter(order=pk)
      for order_goods in order_goods_list:
        goods_instance = models.Goods.objects.get(pk=order_goods.goods.id)
        if instance.order_type == 'depot_in' and order_goods.from_depot == None:
          goods_instance.stock = goods_instance.stock - order_goods.count
        elif order_goods.from_depot != None:
          tmp_count = order_goods.count
          while tmp_count > 0:
            current = models.GoodsRecord.objects.filter(
              record_type='depot_in',
              goods=order_goods.goods,
              leave_count__gt=0,
              record_depot=order_goods.from_depot,
            ).order_by('-record_time').first()
            leave_count = current.count - order_goods.count
            if leave_count >= 0:
              current.leave_count = leave_count
              current.save()
              tmp_count = 0
            else:
              current.leave_count = 0
              current.save()
              tmp_count = tmp_count - current.leave_count
        elif instance.order_type == 'depot_out':
          tmp_count = order_goods.count
          while tmp_count > 0:
            current = models.GoodsRecord.objects.filter(
              record_type='depot_in',
              goods=order_goods.goods,
              leave_count__gt=0,
              record_depot=order_goods.operate_depot,
            ).order_by('-record_time').first()
            leave_count = current.count - order_goods.count
            if leave_count >= 0:
              current.leave_count = leave_count
              current.save()
              tmp_count = 0
            else:
              current.leave_count = 0
              current.save()
              tmp_count = tmp_count - current.leave_count
          goods_instance.stock = goods_instance.stock + order_goods.count
        goods_instance.save()
      self.perform_destroy(instance)
      return Response(u'删除成功', status.HTTP_201_CREATED)
    except Http404:
      pass
    return Response(status=status.HTTP_204_NO_CONTENT)

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
      print(goods.get('shop', None), '2333')
      instance = models.Goods.objects.get(pk=goods['goods_id'])
      data = dict(
        goods=goods['goods_id'],
        count=goods['count'],
        price=goods.get('price', 0),
        unit=goods.get('unit', instance.unit),
        spec=goods.get('spec', instance.spec),
        order=order_data.id,
        operate_depot = goods.get('operate_depot', None),
        supplier=goods.get('supplier', None),
        shop=goods['shop'],
        from_depot=goods.get('from_depot', None),
        production_date=goods.get('production_date', None),
        expiration_date=goods.get('expiration_date', None),
      )
      record_data = dict(
        record_type=req_data.get('order_type', 'depot_in'),
        record_time=operate_time,
        order=order_data.id,
        supplier=goods.get('supplier', None),
        count=goods['count'],
        goods=goods['goods_id'],
        price=goods.get('price', 0),
        operator_account=operator.phone,
        record_depot=goods.get('operate_depot', None),
        from_depot=goods.get('from_depot', None),
        remarks=req_data.get('remarks', ''),
        unit=goods.get('unit', instance.unit),
        spec=goods.get('spec', instance.spec),
        shop=goods['shop'],
        production_date=goods.get('production_date', None),
        expiration_date=goods.get('expiration_date', None),
      )
      amount = 0
      stock = instance.stock
      if req_data['order_type'] == 'depot_in' and goods['from_depot'] == None:
        stock = instance.stock + goods['count']
        amount = goods['count'] * goods['price']   
      elif req_data['order_type'] == 'depot_out':
        if instance.stock - goods['count'] < 0:
          raise rest_serializers.ValidationError({
            'error': u'%s库存不足' % instance.name,
          })
        tmp_count = goods['count']
        while tmp_count > 0:
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
      elif goods['from_depot'] != None:
        if instance.stock - goods['count'] < 0:
          raise rest_serializers.ValidationError({
            'error': u'%s库存不足' % instance.name,
          })
        tmp_count = goods['count']
        while tmp_count > 0:
          # 取出含有剩余量的第一条数据
          current = models.GoodsRecord.objects.filter(
            record_type='depot_in',
            goods = goods['goods_id'],
            count__gt=F('leave_count'),
            record_depot=goods.get('from_depot', None),
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

    