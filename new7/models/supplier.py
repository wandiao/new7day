# coding:utf-8

from django.db import models

from .base import BaseModel

# Create your models here.
class Supplier(BaseModel):
    '''
    供应商
    '''
    SUPPLIER_TYPE = (
        ('formal', u'正规合作'),
        ('finance', u'商铺合作'),
        ('stall', u'摊贩合作'),
    )
    name = models.CharField(
        u'单位名称',
        max_length=20,
        null=True,
        unique=True,
        help_text=u'单位名称',
    )
    type = models.CharField(
        u'供应商分类',
        max_length=20,
        choices=SUPPLIER_TYPE,
        default='a',
        blank=True,
        help_text=u'供应商分类',
    )
    license_code = models.CharField(
        u'执照编号',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'执照编号',
    )
    tontact_phone = models.CharField(
        u'联系电话',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'联系电话',
    )
    contact_name = models.CharField(
        u'联系人',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'联系人',
    )
    address = models.CharField(
        u'公司地址',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'公司地址',
    )
    operator = models.CharField(
        u'经办人',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'经办人',
    )
    operator_name = models.CharField(
        u'经办人电话',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'经办人电话',
    )
    desc = models.CharField(
        u'描述',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'描述',
    )

    common_used = models.BooleanField(
       help_text=u'是否可以被普通员工所用',
       default=True,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'供应商'
        verbose_name_plural = verbose_name

