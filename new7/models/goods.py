# coding:utf-8

from django.db import models

from .base import BaseModel

class Goods(BaseModel):
    '''
    商品
    '''
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
        blank=True,
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
    in_price = models.CharField(
        u'商品进价',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'商品进价',
    )
    sale_price = models.CharField(
        u'商品售价',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'商品售价',
    )

    stock = models.CharField(
        u'库存',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'库存',
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


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = verbose_name

