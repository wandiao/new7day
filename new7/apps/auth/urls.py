# coding=utf-8

from django.conf.urls import url

from rest_framework_jwt import views as jwt_views
from . import views

urlpatterns = [
  url(
    r'^login/',
    views.JWTLoginView.as_view(),
  ),
  url(
    r'^oss/',
    views.OSSView.as_view(),
    name='oss auth',
  )
]