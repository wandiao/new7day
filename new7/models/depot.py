# coding:utf-8

from django.db import models

from .base import BaseModel

class Depot(BaseModel):
    '''
    仓库
    '''
    DEPOT_TYPE = (
        ('main', u'总库'),
        ('branch', u'分库'),
    )
    name = models.CharField(
        u'仓库名称',
        max_length=60,
        null=True,
        unique=True,
        help_text=u'仓库名称',
    )

    type = models.CharField(
        u'仓库类型',
        default='main',
        max_length=20,
        choices=DEPOT_TYPE,
        help_text=u'仓库类型',
    )

    stock = models.IntegerField(
      u'库存',
      default=0,
      help_text=u'库存'
    )

    cubage = models.IntegerField(
      u'容量',
      default=0,
      help_text=u'容量'
    )

    desc = models.CharField(
        u'描述',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'描述',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'仓库'
        verbose_name_plural = verbose_name

