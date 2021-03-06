# coding:utf-8

from django.db import models
import datetime

from .base import BaseModel

# Create your models here.
class Order(BaseModel):
    '''
    订单
    '''

    OPERATE_TYPE = (
        ('depot_in', u'入库'),
        ('depot_out', u'出库'),
    )
    invoice = models.CharField(
        u'票号',
        max_length=100,
        null=True,
        unique=True,
        help_text=u'票号',
    )
    order_unique = models.CharField(
        u'流水号',
        max_length=200,
        null=True,
        unique=True,
        help_text=u'流水号',
    )
    order_type = models.CharField(
        u'订单类型',
        max_length=20,
        choices=OPERATE_TYPE,
        help_text=u'订单类型',
    )
    supplier = models.ForeignKey(
        'new7.Supplier',
        verbose_name=u'供应商',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'供应商',
    )
    tontact_phone = models.CharField(
        u'联系电话',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'联系电话',
    )
    operator = models.CharField(
        u'经办人',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'经办人',
    )
    delivery_date = models.DateTimeField(
        u'交货日期',
        blank=True,
        null=True,
        help_text=u'交货日期',
    )

    deliver_type = models.CharField(
        u'送货方式',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'送货方式',
    )

    deliver_money = models.CharField(
        u'运费',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'运费',
    )

    deliver_address = models.CharField(
        u'收货地址',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'收货地址',
    )

    status = models.CharField(
        u'订单状态',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'订单状态',
    )

    depot = models.ForeignKey(
        'new7.Depot',
        verbose_name=u'仓库',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'仓库',
    )

    # code = models.CharField(
    #     u'编号',
    #     max_length=200,
    #     null=True,
    #     blank=True,
    #     help_text=u'编号',
    # )

    # brand = models.CharField(
    #     u'品名',
    #     max_length=200,
    #     null=True,
    #     blank=True,
    #     help_text=u'品名',
    # )
    # specification = models.CharField(
    #     u'规格',
    #     max_length=200,
    #     null=True,
    #     blank=True,
    #     help_text=u'规格',
    # )
    # unit = models.CharField(
    #     u'单位',
    #     max_length=200,
    #     null=True,
    #     blank=True,
    #     help_text=u'单位',
    # )
    # price = models.CharField(
    #     u'单价',
    #     max_length=200,
    #     null=True,
    #     blank=True,
    #     help_text=u'单价',
    # )
    total_price = models.DecimalField(
        u'总金额',
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text=u'总金额',
    )
    total_count = models.DecimalField(
      u'总数量',
      default=0,
      max_digits=10,
      decimal_places=2,
      help_text=u'总数量'
    )
    pay_type = models.CharField(
        u'支付方式',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'支付方式',
    )
    pay_from = models.CharField(
        u'支付来源',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'支付来源',
    )
    is_pay = models.CharField(
        u'是否支付',
        max_length=10,
        null=True,
        blank=True,
        help_text=u'是否支付',
    )
    # production_date = models.DateTimeField(
    #     u'生产日期',
    #     blank=True,
    #     null=True,
    #     help_text=u'生产日期',
    # )
    # expired_date = models.DateTimeField(
    #     u'有效期',
    #     blank=True,
    #     null=True,
    #     help_text=u'有效期',
    # )
    remark = models.CharField(
        u'备注',
        max_length=500,
        null=True,
        blank=True,
        help_text=u'备注',
    )

    is_closed = models.BooleanField(
        u'订单是否完成',
        default=False,
        blank=True,
        help_text=u'订单是否完成',
    )

    flag = models.CharField(
        u'订单有效标识',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'订单有效标识',
    )

    trade_no = models.CharField(
        u'在线支付流水号',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'在线支付流水号',
    )

    is_refond = models.BooleanField(
        u'是否退款',
        default=False,
        blank=True,
        help_text=u'是否退款',
    )

    def __str__(self):
        return self.invoice

    class Meta:
        verbose_name = u'订单'
        verbose_name_plural = verbose_name

class OrderGoods(BaseModel):
    '''
    订单商品
    '''
    order = models.ForeignKey(
        'new7.Order',
        verbose_name=u'订单',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='order_goods',
        help_text=u'订单',
    )
    goods = models.ForeignKey(
        'new7.Goods',
        verbose_name=u'商品',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'商品',
    )

    count = models.DecimalField(
      u'数量',
      default=1,
      max_digits=10,
      decimal_places=2,
      help_text=u'数量'
    )

    price = models.DecimalField(
        u'价格',
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text=u'价格',
    )

    unit = models.CharField(
        u'单位',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'单位',
    )

    operate_depot = models.ForeignKey(
        'new7.Depot',
        verbose_name=u'操作仓库',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='operate_depot',
        help_text=u'操作仓库',
    )

    from_depot = models.ForeignKey(
        'new7.Depot',
        verbose_name=u'来源仓库',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='from_depot1',
        help_text=u'来源仓库',
    )

    supplier = models.ForeignKey(
        'new7.Supplier',
        verbose_name=u'供应商',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'供应商',
    )

    shop =  models.ForeignKey(
        'new7.Shop',
        verbose_name=u'店面',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'店面',
    )

    production_date = models.DateField(
        u'生产日期',
        blank=True,
        null=True,
        help_text=u'生产日期',
    )

    expiration_date = models.DateField(
        u'过期日期',
        blank=True,
        null=True,
        help_text=u'过期日期',
    )

    @property
    def expirate_status(self):
        if self.expiration_date:
            if datetime.datetime.now() > self.expiration_date:
                return True
        return False


    class Meta:
        verbose_name = u'订单商品'
        verbose_name_plural = verbose_name



