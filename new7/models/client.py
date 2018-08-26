# coding:utf-8

from django.db import models

from .base import BaseModel

class Client(BaseModel):
    '''
    客户
    '''
    name = models.CharField(
        u'客户名称',
        max_length=20,
        null=True,
        unique=True,
        help_text=u'客户名称',
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
        u'地址',
        max_length=20,
        null=True,
        blank=True,
        help_text=u'地址',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'客户'
        verbose_name_plural = verbose_name

