# -*- coding: utf-8 -*-
from __future__ import absolute_import
from import_export import resources
from new7.models import GoodsRecord
from import_export.fields import Field


class ShopCostResource(resources.ModelResource):

  def get_export_headers(self):
    return [u'店面名称', u'商品名称', u'商品数量', u'商品成本']
  class Meta:
    model = GoodsRecord
    fields = ('shop__name','goods__name', 'count', 'amount')
    # export_order = ('shop__name')