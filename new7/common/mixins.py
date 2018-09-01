# coding: utf-8

from __future__ import absolute_import

from django.contrib.contenttypes.models import ContentType
from django.db.models import (
    Sum,
    When,
    Case,
    Count,
    IntegerField,
)
from rest_framework import serializers

from new7 import models
from utils.common_utils import get_date_or_datetime
from utils import (
    regex,
    defines,
)


class DateTimeFieldsSerializerMixin(serializers.Serializer):
    create_time = serializers.DateTimeField(
        format=defines.COMMON_TIME_STRING,
        read_only=True,
        help_text=u'创建时间',
    )
    update_time = serializers.DateTimeField(
        format=defines.COMMON_TIME_STRING,
        read_only=True,
        help_text=u'更新时间',
    )


class SimpleFakeDeleteMixin(object):

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()



class CityProvinceNameSerializerMixin(serializers.Serializer):
    province_id = serializers.IntegerField(
        source='city.province.id',
        read_only=True,
    )
    province_name = serializers.CharField(
        source='city.province.name',
        read_only=True,
    )
    province_short_name = serializers.CharField(
        source='city.province.short_name',
        read_only=True,
    )


class ValidateOrganizationName(serializers.Serializer):
    def validate_name(self, value):
        model = self.Meta.model
        if not self.instance:
            if model.objects.filter(name=value, deleted=False).exists():
                raise serializers.ValidationError(u'重复的名字')
        else:
            if model.objects.filter(name=value, deleted=False).exclude(id=self.instance.id):
                raise serializers.ValidationError(u'重复的名字')
        return value


class RelatedFakeDeleteMixin(object):

    def perform_destroy(self, instance):
        for related_object in instance._meta.related_objects:
            model = related_object.related_model
            if model.__name__ in ['TruckOperateRecord']:
                continue
            field_name = related_object.field.name
            params = {field_name: instance}
            if model.objects.filter(**params):
                raise serializers.ValidationError({
                    'error': u'删除对象有相关联的%s，请更改后再删除' % model._meta.verbose_name,
                })
        instance.deleted = True
        instance.save()


class OnePhonePerOneProfileMixin(object):

    def validate_phone(self, value):
        if not regex.is_mobile(value):
            raise serializers.ValidationError(u'请正确填写手机号')
        need_to_check_phone_exists = True
        if self.instance:  # update
            if value == self.instance.phone:
                need_to_check_phone_exists = False
        if need_to_check_phone_exists:
            if models.Profile.objects.filter(
                phone=value,
                deleted=False,
            ).exists():
                raise serializers.ValidationError(u'该手机号已经存在，不能创建')
        return value
