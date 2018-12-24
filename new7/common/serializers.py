#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from new7 import models
from django.db.transaction import atomic


from . import mixins

class ProfileSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Profile
    fields = (
      'id',
      'user',
      'phone',
      'name',
      'code',
      'gender',
      'address',
      'salary',
      'depot',
      'role',
      'birth',
      'desc',
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
            'code',
            'role',
            'depot',
            'gender',
            'address',
            'salary',
            'birth',
            'desc',
        )

    def validate(self, data):
        phone = data.get('phone')
        if 'role' in data:
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
            'phone',
            'name',
            'role',
            'code',
            'depot',
            'gender',
            'address',
            'salary',
            'birth',
            'desc',
        )

    def validate_phone(self, value):
        if models.Profile.objects.filter(phone=value, deleted=False).exclude(id=self.instance.id):
            raise serializers.ValidationError(u'该手机号已经存在')
        return value

class ShopSerializer(serializers.ModelSerializer):
  contact_user_name = serializers.CharField(
    source='contact_user.name',
    read_only=True
  )
  class Meta:
    model = models.Shop
    fields = (
      'id',
      'name',
      'type',
      'contact_user',
      'contact_user_name',
      'contact_phone',
      'address',
      'staff_num',
    )

class GoodsSerializer(serializers.ModelSerializer):
  last_operator_name = serializers.CharField(
    source='last_operator.name',
    read_only=True,
    help_text=u'上次操作人姓名',
  )
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
      'warn_stock',
      'unit',
      'spec',
      'desc',
      'is_book',
      'last_operator',
      'last_operator_name',
      'last_operate_type',
      'last_operate_time',
      'last_price',
    )

# 库存
class GoodsStockSerializer(serializers.ModelSerializer):
  last_operator_name = serializers.CharField(
    source='last_operator.name',
    read_only=True,
    help_text=u'上次操作人姓名',
  )
  current_depot_stock = serializers.IntegerField(
    default=0,
    help_text=u'当前仓库库存',
  )
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
      'stock_status',
      'warn_stock',
      'last_operator',
      'last_operator_name',
      'last_operate_type',
      'last_operate_time',
      'last_price',
      'current_depot_stock',
    )

# 成本
class GoodsCostSerializer(serializers.Serializer):
  goods = serializers.CharField(
    max_length=20,
    help_text=u'商品id',
  )
  goods__name = serializers.CharField(
    max_length=20,
    help_text=u'商品名称',
  )
  count = serializers.IntegerField(
    help_text=u'进货数量',
  )
  cost = serializers.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    help_text=u'进货成本',
  )

  unit = serializers.CharField(
    max_length=20,
    required=False,
    help_text=u'单位',
  )

  spec = serializers.CharField(
    max_length=20,
    required=False,
    help_text=u'规格',
  )

  used_count = serializers.IntegerField(
    help_text=u'使用数量',
  )

  used_cost = serializers.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    help_text=u'使用成本',
  )

  damaged_count = serializers.IntegerField(
    help_text=u'报损数量',
  )

  damaged_cost = serializers.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    help_text=u'报损成本',
  )

# 成本统计
class  GoodsStatsSerializer(serializers.Serializer):
  month = serializers.IntegerField(
    help_text=u'月份',
  )
  count = serializers.IntegerField(
    help_text=u'进货数量',
  )
  cost = serializers.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    help_text=u'进货成本',
  )

  used_count = serializers.IntegerField(
    help_text=u'使用数量',
  )

  used_cost = serializers.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    help_text=u'使用成本',
  )

  damaged_count = serializers.IntegerField(
    help_text=u'报损数量',
  )

  damaged_cost = serializers.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    help_text=u'报损成本',
  )

  



class GoodsRecordSerializer(serializers.ModelSerializer):
  goods_name = serializers.CharField(
    source='goods.name',
    read_only=True
  )
  record_depot_name = serializers.CharField(
    source='record_depot.name',
    read_only=True
  )
  shop = ShopSerializer(
    many=False,
    help_text=u'订单商品',
    read_only=True,
  )
  supplier_name = serializers.CharField(
    source='supplier.name',
    read_only=True
  )
  class Meta:
    model = models.GoodsRecord
    fields = (
      'id',
      'goods',
      'order',
      'goods_name',
      'count',
      'leave_count',
      'unit',
      'spec',
      'price',
      'record_type',
      'record_depot',
      'record_depot_name',
      'record_time',
      'record_source',
      'operator_account',
      'shop',
      'supplier',
      'supplier_name',
      'remarks',
      'amount',
      'production_date',
      'expiration_date',
      'expirate_status',
    )

class GoodsDamagedSerializer(serializers.ModelSerializer):
  goods_name = serializers.CharField(
    source='goods.name',
    read_only=True
  )
  goods_unit = serializers.CharField(
    source='goods.unit',
    read_only=True
  )
  goods_spec = serializers.CharField(
    source='goods.spec',
    read_only=True
  )
  damaged_depot_name = serializers.CharField(
    source='damaged_depot.name',
    read_only=True
  )
  operator_name = serializers.CharField(
    source='operator.name',
    read_only=True
  )
  damaged_shop_name = serializers.CharField(
    source='damaged_shop.name',
    read_only=True
  )
  class Meta:
    model = models.GoodsDamaged
    fields = (
      'id',
      'goods',
      'goods_name',
      'count',
      'price',
      'damaged_depot',
      'damaged_depot_name',
      'damaged_shop',
      'damaged_shop_name',
      'report_time',
      'operator',
      'operator_name',
      'remarks',
      'amount',
      'goods_spec',
      'goods_unit',
    )


class OrderGoodsListSerializer(serializers.Serializer):
  goods_id = serializers.CharField(
    max_length=20,
    help_text=u'商品id',
  )
  count = serializers.IntegerField(
    required=True,
    help_text=u'数量',
  )
  price = serializers.FloatField(
    help_text=u'价格',
  )
  unit = serializers.CharField(
    max_length=20,
    required=False,
    help_text=u'单位',
  )

  spec = serializers.CharField(
    max_length=20,
    required=False,
    help_text=u'规格',
  )

  operate_depot = serializers.CharField(
    max_length=20,
    required=False,
    help_text=u'操作仓库',
  )

  shop = serializers.CharField(
    max_length=20,
    required=False,
    help_text=u'出货店面',
  )

  production_date = serializers.DateField(
    required=False,
    help_text=u'生产日期',
    allow_null=True,
  )

  expiration_date = serializers.DateField(
    required=False,
    help_text=u'过期日期',
    allow_null=True,
  )



class OrderGoodsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.OrderGoods
    fields = (
      'order',
      'goods',
      'count',
      'price',
      'unit',
      'operate_depot',
      'shop',
    )

class OrderGoodsDetailSerializer(serializers.ModelSerializer):
  goods = GoodsSerializer(
    many=False,
    help_text=u'订单商品',
    read_only=True
  )
  operate_depot_name = serializers.CharField(
    source='operate_depot.name',
    read_only=True,
  )
  shop_name = serializers.CharField(
    source='shop.name',
    read_only=True,
  )
  class Meta:
    model = models.OrderGoods
    fields = (
      'order',
      'goods',
      'count',
      'price',
      'unit',
      'operate_depot',
      'operate_depot_name',
      'shop',
      'shop_name',
      'production_date',
      'expiration_date',
      'expirate_status',
    )


class OrderSerializer(serializers.ModelSerializer):
  supplier_name = serializers.CharField(
    source='supplier.name',
    read_only=True
  )
  order_goods = OrderGoodsDetailSerializer(
    many=True,
    help_text=u'订单商品',
    read_only=True
  )
  class Meta:
    model = models.Order
    fields = (
      'id',
      'invoice',
      'order_unique',
      'order_type',
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
      # 'code',
      # 'brand',
      # 'specification',
      # 'unit',
      # 'price',
      'total_price',
      'total_count',
      # 'production_date',
      # 'expired_date',
      'remark',
      'order_goods',
    )

class OrderCreateSerializer(serializers.ModelSerializer):
  goods_info = OrderGoodsListSerializer(
        many=True,
        help_text=u'商品信息列表',
        required=False,
    )
  class Meta:
    model = models.Order
    fields = (
      'id',
      'invoice',
      'order_unique',
      'order_type',
      'supplier',
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
      # 'code',
      # 'brand',
      # 'specification',
      # 'unit',
      # 'price',
      'total_price',
      'total_count',
      # 'production_date',
      # 'expired_date',
      'remark',
      'goods_info',
    )
  @atomic
  def create(self, validate_data):
      goods_info = validate_data.pop('goods_info')
      instance = models.Order.objects.create(**validate_data)
      return instance

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
      'operator',
      'operator_name',
      'license_code',
      'desc',
      'common_used',
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
      'desc',      
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
      'name',
      'type',
      'stock',
      'cubage',
      'desc',
      'depot_keepers',
    )


class FileImportExportSerializer(serializers.Serializer):
    file = serializers.FileField(
        help_text=u'file',
    )