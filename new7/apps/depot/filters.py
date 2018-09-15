# -*- coding: utf-8 -*-

import django_filters

from new7 import models


class DepotFilterSet(django_filters.FilterSet):
  class Meta:
    model = models.Depot
    fields = (
      'name',
      'type',
    )
