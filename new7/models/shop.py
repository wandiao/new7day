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

    operator = models.ForeignKey(
        'new7.Profile',
        verbose_name=u'操作人员',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'操作人员',
    )

    def __str__(self):
        return self.create_time.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        verbose_name = u'店面收入'
        verbose_name_plural = verbose_name

class ShopInventory(BaseModel):
    '''
    店面盘点
    '''
    shop = models.ForeignKey(
        'new7.Shop',
        verbose_name=u'店面',
        on_delete=models.CASCADE,
        null=False,
        help_text=u'店面',
    )

    goods = models.ForeignKey(
        'new7.Goods',
        verbose_name=u'商品',
        on_delete=models.CASCADE,
        null=False,
        help_text=u'商品',
    )

    stock = models.DecimalField(
      u'库存',
      default=0,
      max_digits=10,
      decimal_places=2,
      help_text=u'库存'
    )

    month = models.IntegerField(
        default=0,
        help_text=u'月份',
    )

    price = models.DecimalField(
        u'商品价格',
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text=u'商品价格',
    )

    amount = models.FloatField(
        u'商品成本',
        default=0,
        help_text=u'商品成本',
    )

    operator = models.ForeignKey(
        'new7.Profile',
        verbose_name=u'操作人员',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'操作人员',
    )

    def save(self, *args, **kwargs):
        self.amount = self.price * self.stock
        super().save(*args, **kwargs)



    def __str__(self):
        return self.create_time.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        verbose_name = u'店面盘点'
        verbose_name_plural = verbose_name


