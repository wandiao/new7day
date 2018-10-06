# coding: utf-8

import datetime

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken, APIView

from django.views.generic import View

from rest_framework.response import Response

from new7.common import (
    serializers as common_serializers,
)
from django.http import JsonResponse
from . import serializers

class JWTLoginView(ObtainJSONWebToken):
  '''
    登录接口
  '''
  serializer_class = serializers.LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if serializer.is_valid():
      user = serializer.object.get('user') or request.user
      user.last_login = datetime.datetime.now()
      user.save()
      token = serializer.object.get('token')
      response_data = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(token, user, request)
      profile_serializer = common_serializers.ProfileDetailSerializer(instance=user.profile)
      response_data.update({
        'expires_in': api_settings.JWT_EXPIRATION_DELTA,
        'profile': profile_serializer.data
      })
      return Response(response_data)
    return Response(serializer.errors, status=400)

class OSSView(APIView):
  """
  oss文件上传
  """
  def get(self, request):
    return Response(dict(
      accessKeyId='LTAIYMdVVBM1Uzj2',
      accessKeySecret='v6zlAlinTrFR0DHiWf7upkhZWAxbfg',
      region='oss-cn-beijing',
      bucket='new7day',
    ))



