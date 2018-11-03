# coding:utf-8

from django.db import models

from .base import BaseModel

class Goods(BaseModel):
    '''
    商品
    '''

    OPERATE_TYPE = (
        ('depot_in', u'入库'),
        ('depot_out', u'出库'),
    )

    name = models.CharField(
        u'商品名称',
        max_length=100,
        null=True,
        unique=True,
        help_text=u'商品名称',
    )

    short_name = models.CharField(
        u'商品简称',
        max_length=100,
        null=True,
        help_text=u'商品简称',
    )

    code = models.CharField(
        u'商品编码',
        null=True,
        unique=True,
        max_length=100,
        help_text=u'商品编码',
    )


    img = models.CharField(
        u'商品图片',
        max_length=500,
        null=True,
        blank=True,
        help_text=u'商品图片',
    )
    brand = models.CharField(
        u'品牌',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'品牌',
    )
    in_price = models.DecimalField(
        u'商品进价',
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text=u'商品进价',
    )
    sale_price = models.DecimalField(
        u'商品售价',
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text=u'商品售价',
    )

    stock = models.IntegerField(
      u'库存',
      default=0,
      help_text=u'库存'
    )

    last_operator = models.ForeignKey(
        'new7.Profile',
        verbose_name=u'最近操作人',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'最近操作人',
    )

    last_operate_type = models.CharField(
        u'最近操作类型',
        null=True,
        max_length=20,
        choices=OPERATE_TYPE,
        help_text=u'最近操作类型',
    )

    last_operate_time = models.DateTimeField(
        u'上次操作时间',
        blank=True,
        null=True,
        help_text=u'上次操作时间',
    )

    last_price =  models.DecimalField(
        u'上次价格',
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text=u'上次价格',
    )

    unit = models.CharField(
        u'单位',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'单位',
    )

    spec = models.CharField(
        u'规格',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'规格',
    )

    desc = models.CharField(
        u'描述',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'描述',
    )

    is_book = models.BooleanField(
        u'是否预定',
        default=False,
        blank=True,
        help_text=u'是否预定',
    )

    stock_status = models.IntegerField(
      u'库存状态',
      default=1,
      help_text=u'库存状态'
    )

    def save(self, *args, **kwargs):
        if self.stock < 10:
            self.stock_status = 0
        else:
            self.stock_status = 1
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = verbose_name


class GoodsRecord(BaseModel):
    '''
    商品操作
    '''

    OPERATE_TYPE = (
        ('depot_in', u'入库'),
        ('depot_out', u'出库'),
    )
    goods =  models.ForeignKey(
        'new7.Goods',
        verbose_name=u'商品',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'商品',
    )

    record_type = models.CharField(
        u'记录类型',
        default='depot_in',
        max_length=20,
        choices=OPERATE_TYPE,
        help_text=u'操作类型',
    )

    order = models.ForeignKey(
        'new7.Order',
        verbose_name=u'所属订单',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'所属订单',
    )

    count = models.IntegerField(
      u'数量',
      default=0,
      help_text=u'数量'
    )

    leave_count = models.IntegerField(
      u'出库数量',
      default=0,
      help_text=u'出库数量'
    )

    price = models.FloatField(
        u'价格',
        blank=True,
        null=True,
        help_text=u'价格',
    )

    unit = models.CharField(
        u'单位',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'单位',
    )

    operator_account = models.CharField(
        u'操作员账号',
        max_length=20,
        null=True,
        help_text=u'操作员账号',
    )

    record_time = models.DateTimeField(
        u'记录时间',
        blank=True,
        null=True,
        help_text=u'记录时间',
    )

    record_source = models.CharField(
        u'操作来源',
        max_length=50,
        blank=True,
        default='',
        help_text=u'操作来源',
    )

    record_depot = models.ForeignKey(
        'new7.Depot',
        verbose_name=u'操作仓库',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'操作仓库',
    )

    remarks = models.TextField(
        u'备注',
        blank=True,
        default='',
        help_text=u'备注',
    )

    amount = models.DecimalField(
        u'成本',
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text=u'成本',
    )

    def save(self, *args, **kwargs):
        self.amount = self.price * self.count
        super().save(*args, **kwargs)

    def __str__(self):
        return self.create_time.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        verbose_name = u'商品记录'
        verbose_name_plural = verbose_name

    
