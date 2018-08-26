# coding:utf-8

from django.db import models

from .base import BaseModel

class Depot(BaseModel):
    '''
    仓库
    '''
    DEPOT_TYPE = (
        ('main', u'在途'),
        ('branch', u'总库'),
    )
    name = models.CharField(
        u'仓库名称',
        max_length=20,
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

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'供应商'
        verbose_name_plural = verbose_name

