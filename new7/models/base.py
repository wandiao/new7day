#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class BaseModel(models.Model):
  create_time = models.DateTimeField(
    u'创建时间',
    auto_now_add=True,
    blank=True,
    null=True,
    help_text=u'创建时间',
  )
  update_time = models.DateTimeField(
    u'更新时间',
    auto_now=True,
    blank=True,
    null=True,
    help_text=u'更新时间',
  )

  @property
  def self(self):
    return self

  class Meta:
    abstract = True

class DeletedMixin(models.Model):
  deleted = models.BooleanField(
    u'是否已删除',
    default=False,
    blank=True,
    help_text=u'是否已删除',
  )

  class Meta:
    abstract = True
