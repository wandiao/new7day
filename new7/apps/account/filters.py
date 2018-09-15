# -*- coding: utf-8 -*-

import django_filters

from new7 import models


class ProfileFilterSet(django_filters.FilterSet):
  class Meta:
    model = models.Profile
    fields = (
      'name',
      'code',
    )
