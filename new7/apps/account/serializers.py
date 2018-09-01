# coding: utf-8

import shortuuid

from django.db import transaction
from django.contrib.auth.models import User, Permission

from rest_framework import serializers

from new7 import models
from new7.common.validators import validate_phone


class CreateAuthUserMixin(object):

    def create_user(self, password, username=None):
        if username is None:
            username = str(shortuuid.uuid())

        user = User.objects.create_user(
            username=username,
            password=password,
        )
        return user


class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'password',
            'last_login',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'last_login': {'read_only': True},
        }


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(
        label=u'旧密码',
        write_only=True,
    )
    password = serializers.CharField(
        label=u'新密码',
        write_only=True,
        min_length=8,
    )
    confirm_password = serializers.CharField(
        label=u'确认密码',
        write_only=True,
        min_length=8,
    )

    def validate_old_password(self, old_password):
        user = self.context['user']
        if not user.check_password(old_password):
            raise serializers.ValidationError('旧密码有误')
        return old_password

    def validate(self, data):
        password = data['password']
        confirm_password = data['confirm_password']
        old_password = data['old_password']

        if password != confirm_password:
            raise serializers.ValidationError(u'两次密码不一致')
        elif password == old_password:
            raise serializers.ValidationError(u'新密码与旧密码不能一致，重新输入新密码')
        return data