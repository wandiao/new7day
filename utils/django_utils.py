#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sha
import json

from django.http import HttpResponse
from django.contrib.auth.models import User

from conf import config
from owl import models
from utils import (
    common_utils,
)
from utils.db_connections import (
    set_VIN_FaultSourceModel_Relation,
    set_Fault_Source_Model_Fault_Relation,
)


def verify_weixin(request):
    args = request.GET
    nonce = args.get('nonce', '')
    timestamp = args.get('timestamp', '')
    signature = args.get('signature', '')
    strings = [config.TOKEN, timestamp, nonce]
    strings.sort()
    v_string = ''.join(strings)
    v_string = sha.sha(v_string).hexdigest()
    return v_string == signature


def get_distinct_username():
    username = common_utils.get_uuid()
    if User.objects.filter(username=username).exists():
        return get_distinct_username()
    return username


def create_user(phone):
    username = get_distinct_username()
    user = User.objects.create_user(
        username=username,
        password=phone,
    )
    return user


def get_unicode_code():
    unique_code = common_utils.get_uuid(letters_only=True)
    if models.Fault.objects.filter(unique_code=unique_code).exists():
        return get_unicode_code()
    return unique_code


def create_profile(**kwargs):
    profile = models.Profile.objects.create(**kwargs)
    return profile


def get_or_create_profile(phone, defaults):
    profile, _ = models.Profile.objects.get_or_create(
        phone=phone,
        defaults=defaults
    )
    return profile


def get_fault_code_list(fault_source_model):
    value = fault_source_model
    fault_code_list = [f.fault_code for f in models.Fault.objects.filter(fault_source_model=value)]
    return fault_code_list


class CSVTPLResponse(object):
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

    def __call__(self):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="%s"' % self.filename
        writer = csv.writer(response)
        writer.writerow(self.headers)
        return response


def json_response(data, *args, **kwargs):
    return HttpResponse(json.dumps(data, *args, **kwargs), content_type='application/json; charset=utf-8')


def get_or_set_source_models_dict(redis_conn, vin):
    source_models = redis_conn.hget('VIN_FaultSourceModel_Relation', vin)
    if not source_models:
        truck = models.Truck.objects.filter(
            vin=vin,
        ).first()
        if truck:
            set_VIN_FaultSourceModel_Relation(truck)
            return get_or_set_source_models_dict(redis_conn, vin)
        return None
    return json.loads(source_models)


def get_or_set_fault_info(redis_conn, source_model, fault_code):
    key = '%s_%s' % (source_model, fault_code)  # e.g.: 1_abcd, 101_xyz0
    fault_info = redis_conn.hget('Fault_Source_Model_Fault_Relation', key)
    if not fault_info:
        fault = models.Fault.objects.filter(
            fault_source_model=source_model,
            fault_code=fault_code,
        ).first()
        if fault:
            set_Fault_Source_Model_Fault_Relation(key, fault)
            return get_or_set_fault_info(redis_conn, source_model, fault_code)
        return None
    return json.loads(fault_info)
