# -*- coding: utf-8 -*-

import django_filters

from new7 import models


class GoodsFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Goods
        fields = (
            'name',
            'short_name',
            'code',
            'spec'
        )

class GoodsRecordFilterSet(django_filters.FilterSet):
    goods_id = django_filters.CharFilter(
        name='goods',
    )
    class Meta:
        model = models.GoodsRecord
        fields = (
            'goods_id',
            'record_depot',
            'record_type',
        )