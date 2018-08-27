#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from new7 import models

class OrderSerializer(serializers.ModelSerializer):
  supplier_name = serializers.CharField(
    source='supplier.name',
    read_only=True
  )
  class Meta:
    model = models.Order
    fields = (
      'id',
      'invoice',
      'order_unique',
      'supplier',
      'supplier_name',
      'tontact_phone',
      'operator',
      'delivery_date',
      'deliver_type',
      'deliver_money',
      'deliver_address',
      'status',
      'pay_type',
      'pay_from',
      'is_pay',
      'is_closed',
      'flag',
      'trade_no',
      'is_refond',
      'depot',
      'code',
      'brand',
      'specification',
      'unit',
      'price',
      'total_price',
      'production_date',
      'expired_date',
      'remark'
    )

class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Supplier
    fields = (
      'id',
      'name',
      'type',
      'contact_name',
      'tontact_phone',
      'address',
      'account',
    )

class ClientSeralizer(serializers.ModelSerializer):
  class Meta:
    model = models.Client
    fields = (
      'id',
      'name',
      'contact_name',
      'tontact_phone',
      'address',
    )

class DepotSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Depot
    fields = (
      'id',
      'type',
      'stock',
    )

class GoodsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Goods
    fields = (
      'id',
      'name',
      'code',
      'img',
      'brand',
      'in_price',
      'sale_price',
      'stock',
      'unit',
      'spec',
      'desc',
      'is_book',
    )