#!/usr/bin/env python
# -*- coding: utf-8 -*-

from owl import models
from utils import (
    common_utils,
)
from rest_framework import serializers


def no_auth_perm_needed(cls):
    cls.permission_classes = ()
    cls.authentication_classes = ()
    return cls


def no_perm_needed(cls):
    cls.permission_classes = ()
    return cls


def no_xxx_needed(*names):
    def decorator(cls):
        for name in names:
            setattr(cls, name, ())
        return cls
    return decorator


def need_permission(**kwargs):
    def decorator(f):
        def method(self, *args, **m_kwargs):
            user = self.request.user
            profile = user.profile
            perms = {
                'is_superuser': user.is_superuser,
                'role': profile.role,
            }
            for k, v in kwargs.iteritems():
                if perms.get(k) != v:
                    raise serializers.ValidationError({
                        'error': u'账户类型有误, 不能进行此操作',
                    })
            return f(self, *args, **m_kwargs)
        return method
    return decorator


def need_one_of_permissions(permissions):
    def decorator(f):
        def method(self, *args, **m_kwargs):
            user = self.request.user
            profile = user.profile
            perms = {
                'is_superuser': user.is_superuser,
                'role': profile.role,
            }
            has_perm = False
            for kwargs in permissions:
                if common_utils.dict_has_subset(perms, kwargs):
                    has_perm = True
                    break
            if not has_perm:
                raise serializers.ValidationError({
                    'error': u'账户类型有误, 不能进行此操作',
                })
            return f(self, *args, **m_kwargs)
        return method
    return decorator


def check_entity(key):
    def decorator(f):
        def method(self, *args, **m_kwargs):
            obj = self.request.user.profile.content_object
            instance = self.get_object()
            if isinstance(obj, models.PlatformCompany):
                if isinstance(instance, models.Dealer):
                    return f(self, *args, **m_kwargs)
            if getattr(instance, key, None) != obj:
                raise serializers.ValidationError({
                    'error': u'账户有误, 不能进行此操作',
                })
            return f(self, *args, **m_kwargs)
        return method
    return decorator


def check_entities(keys):
    def decorator(f):
        def method(self, *args, **m_kwargs):
            obj = self.request.user.profile.content_object
            instance = self.get_object()
            if isinstance(obj, models.PlatformCompany):
                if isinstance(instance, models.Dealer):
                    return f(self, *args, **m_kwargs)
            has_perm = False
            for key in keys:
                if getattr(instance, key, None) == obj:
                    has_perm = True
                    break
            if not has_perm:
                raise serializers.ValidationError({
                    'error': u'账户有误, 不能进行此操作',
                })
            return f(self, *args, **m_kwargs)
        return method
    return decorator


def add_read_only_fields(*fields):
    def decorator(cls):
        cls.read_only_fields = fields
        return cls
    return decorator


def rm_paginator_if_needed(cls):
    _get = cls.get

    def get(self, request, *args, **kwargs):
        if request.GET.get('paginator') == '0':
            self._paginator = None
        return _get(self, request, *args, **kwargs)

    cls.get = get
    return cls
