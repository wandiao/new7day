# coding: utf-8

from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from new7 import models

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class LoginSerializer(JSONWebTokenSerializer):
  user_profile_model = models.Profile
  attr = 'profile'

  def authenticate_user(self, credentials):
    user = authenticate(
      user_profile_model=self.user_profile_model,
      **credentials
    )
    return user
  
  def get_user(self, credentials, username_field_value):
    user = self.authenticate_user(credentials)
    if (user):
      return user
    try:
      profile = self.user_profile_model.objects.get(
        phone=username_field_value,
        deleted=False,
      )
      credentials[self.username_field] = profile.user.username
      return self.authenticate_user(credentials)
    except Exception as e:
      print(type(e), e)
  def validate(self, attrs):
    username_field_value = attrs.get(self.username_field)
    credentials = {
      self.username_field: username_field_value,
      'password': attrs.get('password'),
    }
    if all(credentials.values()):
      user = self.get_user(credentials, username_field_value)
      if user:
        if not user.is_active:
          msg = _(u'用户未激活')
          raise serializers.ValidationError(msg)
        if not hasattr(user, self.attr):
          msg = _(u'没有使用该系统的权限')
          raise serializers.ValidationError(msg)
          profile = user.profile
        payload = jwt_payload_handler(user)
        return {
          'token': jwt_encode_handler(payload),
          'user': user,
        }
      else:
        msg = _(u'用户名或密码错误')
        raise serializers.ValidationError(msg)
    else:
      msg = _(u'请填写用户名或密码')
      msg = msg.format(username_field=self.username_field)
      raise serializers.ValidationError(mag)

  

