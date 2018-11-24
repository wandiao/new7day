# coding: utf-8


from django.contrib.auth.models import User
from rest_framework import serializers as rest_serializers

from new7 import models
from utils import (
    common_utils,
    defines,
)

def create_user(phone):
    username = common_utils.get_uuid()
    user = User.objects.create_user(
        username=username,
        password='123456',
    )
    return user


def create_profile(**kwargs):
    profile = models.Profile(**kwargs)
    profile.save()
    return profile


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
                    raise rest_serializers.ValidationError({
                        'error': u'账户类型有误, 不能进行此操作',
                    })
            return f(self, *args, **m_kwargs)
        return method
    return decorator
