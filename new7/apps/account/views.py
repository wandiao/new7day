# coding: utf-8

from rest_framework import (
    viewsets,
    mixins,
)

from new7 import models
from new7.common import serializers as common_serializers
from new7.common.schema import auto_schema, DocParam
from new7.common.utils import (
    create_user,
)

from . import serializers
from . import filters


class ProfileViewSet(viewsets.ModelViewSet):
    """
    账户接口

    retrieve:
    账户详情

    list:
    账户列表

    create:
    新增账户

    partial_update:
    修改账户

    update:
    修改账户

    delete:
    删除账户
    """
    queryset = models.Profile.objects.filter(deleted=False)
    serializer_class = common_serializers.ProfileSerializer
    search_fields = ('name', 'phone')
    filter_class = filters.ProfileFilterSet
    # schema = auto_schema([
    #     DocParam('name', description='名称'),
    #     DocParam('code', description='员工编号'),
    # ])

    def get_queryset(self):
        if self.action == 'list':
            object_id = self.request.user.profile.object_id
            return self.queryset.filter(object_id=object_id)
        return self.queryset

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return common_serializers.ProfileUpdateSerializer
        elif self.action == 'create':
            return common_serializers.ProfileCreateSerializer
        else:
            return self.serializer_class

    def perform_create(self, serializer):
        phone = serializer.validated_data.get('phone')
        role = serializer.validated_data.get('role')
        user = self.request.user
        if user.profile.role != 'super_admin':
            raise rest_serializers.ValidationError({
                'error': u'账户类型有误, 不能创建',
            })
        content_object = user.profile.content_object
        user = create_user(phone)
        serializer.save(
            user=user,
            content_object=content_object,
        )
