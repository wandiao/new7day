# coding:utf-8

from django.db import models

from .base import BaseModel

class Shop(BaseModel):
    '''
    店面
    '''
    SHOP_TYPE = (
        ('direct', u'直营店'),
        ('extra', u'外包店'),
    )
    name = models.CharField(
        u'店面名称',
        max_length=50,
        null=False,
        unique=True,
        help_text=u'店面名称',
    )
    type = models.CharField(
        u'店面类型',
        default='direct',
        max_length=20,
        choices=SHOP_TYPE,
        help_text=u'店面类型',
    )
    contact_user = models.ForeignKey(
        'new7.Profile',
        verbose_name=u'店面负责人',
        on_delete=models.PROTECT,
        null=False,
        help_text=u'店面负责人',
    )
    contact_phone = models.CharField(
        u'联系电话',
        max_length=20,
        null=False,
        help_text=u'联系电话',
    )
    address = models.CharField(
        u'店面地址',
        max_length=100,
        null=False,
        help_text=u'店面地址',
    )

    staff_num = models.IntegerField(
      u'店面人数',
      help_text=u'店面人数'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'店面'
        verbose_name_plural = verbose_name


class ShopIncome(BaseModel):
    '''
    店面收入
    '''
    shop = models.ForeignKey(
        'new7.Shop',
        verbose_name=u'店面',
        on_delete=models.PROTECT,
        null=False,
        help_text=u'店面',
    )

    income = models.DecimalField(
        u'收入',
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text=u'收入',
    )

    def __str__(self):
        return self.create_time.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        verbose_name = u'店面收入'
        verbose_name_plural = verbose_name


