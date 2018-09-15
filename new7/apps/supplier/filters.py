# -*- coding: utf-8 -*-

import django_filters

from new7 import models


class SupplierFilterSet(django_filters.FilterSet):
  class Meta:
    model = models.Supplier
    fields = (
      'name',
      'type',
    )
