# coding:utf-8

from django.db import models

from .base import BaseModel

# Create your models here.
class Order(BaseModel):
    '''
    订单
    '''
    invoice = models.CharField(
        u'票号',
        max_length=100,
        null=True,
        unique=True,
        help_text=u'单位名称',
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

    depot = models.CharField(
        u'仓库',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'仓库',
    )

    code = models.CharField(
        u'编号',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'编号',
    )

    brand = models.CharField(
        u'品名',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'品名',
    )
    specification = models.CharField(
        u'规格',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'规格',
    )
    unit = models.CharField(
        u'单位',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'单位',
    )
    price = models.CharField(
        u'单价',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'单价',
    )
    total_price = models.CharField(
        u'金额',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'金额',
    )
    production_date = models.DateTimeField(
        u'生产日期',
        blank=True,
        null=True,
        help_text=u'生产日期',
    )
    expired_date = models.DateTimeField(
        u'有效期',
        blank=True,
        null=True,
        help_text=u'有效期',
    )
    remark = models.CharField(
        u'备注',
        max_length=500,
        null=True,
        blank=True,
        help_text=u'备注',
    )

    def __str__(self):
        return self.invoice

    class Meta:
        verbose_name = u'订单'
        verbose_name_plural = verbose_name

