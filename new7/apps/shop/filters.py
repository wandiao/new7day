# -*- coding: utf-8 -*-

import django_filters

from new7 import models


class ShopFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Shop
        fields = (
            'type',
        )

class ShopInventoryFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.ShopInventory
        fields = (
            'month',
            'shop',
        )