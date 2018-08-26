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
      'supplier',
      'supplier_name',
      'tontact_phone',
      'operator',
      'delivery_date',
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