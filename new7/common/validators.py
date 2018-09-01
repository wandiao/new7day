# coding: utf-8


from rest_framework import serializers

from .regex import error_phone


def validate_phone(phone):
    if error_phone(phone):
        raise serializers.ValidationError('电话有误')


def validate_phones(phones):
    if len(set(phones)) < len(phones):
        raise serializers.ValidationError('电话号码有重复')
    for phone in phones:
        if error_phone(phone):
            raise serializers.ValidationError('电话有误')
