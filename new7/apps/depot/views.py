# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from new7 import models
from new7.common import serializers as common_serializers

class ClientViewSet(viewsets.ModelViewSet):
  """
    仓库接口
  """
  queryset = models.Depot.objects.all()
  serializer_class = common_serializers.DepotSerializer

