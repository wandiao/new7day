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
        field_name='goods',
    )

    expiration_date = django_filters.DateFilter(
        field_name='expiration_date',
        lookup_expr='lte',
        label=u'过期时间',
    )
    class Meta:
        model = models.GoodsRecord
        fields = (
            'goods_id',
            'record_depot',
            'record_type',
            'shop',
        )


class GoodsDamagedFilterSet(django_filters.FilterSet):
    goods_id = django_filters.CharFilter(
        field_name='goods',
    )
    class Meta:
        model = models.GoodsDamaged
        fields = (
            'goods_id',
            'damaged_depot',
            'damaged_shop',
        )