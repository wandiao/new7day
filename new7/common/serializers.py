#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from new7 import models


from . import mixins

class ProfileSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Profile
    fields = (
      'id',
      'user',
      'phone',
      'name',
      'role',
      'phone_verified',
    )

ProfileDetailSerializer = ProfileSerializer

class ProfileCreateSerializer(
    mixins.OnePhonePerOneProfileMixin,
    serializers.ModelSerializer
):
    class Meta:
        model = models.Profile
        read_only_fields = (
            'id',
            'user',
            'phone_verified',
        )
        fields = read_only_fields + (
            'phone',
            'name',
            'role',
            'depot',
        )

    def validate(self, data):
        phone = data.get('phone')
        role = data['role']
        if role == 'warekeeper':
            if 'depot' not in data.keys():
                raise serializers.ValidationError('没有指定库房')
        if models.Profile.objects.filter(
            phone=phone,
            deleted=False,
        ):
            raise serializers.ValidationError(u'该手机号已经存在，不能创建')
        return data


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        read_only_fields = (
            'id',
            'user',
            'phone_verified',
        )
        fields = read_only_fields + (
            'name',
            'role',
            'phone',
            'depot',
        )

    def validate_phone(self, value):
        if models.Profile.objects.filter(phone=value, deleted=False).exclude(id=self.instance.id):
            raise serializers.ValidationError(u'该手机号已经存在')
        return value



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
  depot_keepers = ProfileSerializer(
    many=True,
    read_only=True,
    help_text=u'库管员'
  )
  class Meta:
    model = models.Depot
    fields = (
      'id',
      'type',
      'stock',
      'cubage',
      'depot_keepers',
    )

class GoodsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Goods
    fields = (
      'id',
      'name',
      'short_name',
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