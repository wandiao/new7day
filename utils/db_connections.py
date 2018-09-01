#!/usr/bin/python
# coding=utf-8

import json
import redis

from conf import config
from utils import defines


def get_redis():
    return redis.Redis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=config.REDIS_DB,
        password=config.REDIS_PASSWORD,
        socket_timeout=20,
    )


def get_redis_pool():
    redis_pool = redis.ConnectionPool(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        password=config.REDIS_PASSWORD,
        db=config.REDIS_DB
    )
    return redis.Redis(connection_pool=redis_pool)


def validate_vin_in_redis(data, redis_conn=None):
    if not redis_conn:
        redis_conn = get_redis_pool()
    vin = (data or {}).get('vin')
    if not vin:
        return
    if redis_conn.hexists('VIN_MainFactory_Relation', vin):
        return data


def set_MainFactory_Alert_Level_Settings(main_factory):  # noqa
    redis_conn = get_redis_pool()
    redis_key = 'MainFactory_Alert_Level_Settings'
    try:
        data = json.dumps(main_factory.alert_level_settings or defines.DEFAULT_ALERT_LEVEL_SETTINGS)
        redis_conn.hset(redis_key, main_factory.id, data)
    except Exception as e:
        print type(e), e


def set_VIN_Organization_Relation(truck):  # noqa
    try:
        redis_conn = get_redis_pool()
        vin = truck.vin
        main_factory_id = truck.main_factory_id
        division_id = truck.division_id
        data = {}
        if division_id:
            data.update(division_id=division_id)
        if main_factory_id:
            data.update(
                main_factory_id=truck.main_factory_id,
                platform_company_id=truck.main_factory.platform_company_id,
            )
            redis_conn.hset('VIN_MainFactory_Relation', vin, main_factory_id)
        if data:
            redis_conn.hset('VIN_Organization_Relation', vin, json.dumps(data, ensure_ascii=False))
    except Exception as e:
        print type(e), e


def set_VIN_PublicationNumber_Relation(truck):  # noqa
    try:
        redis_conn = get_redis_pool()
        vin = truck.vin
        if truck.truck_model:
            publication_number = truck.truck_model.publication_number
        else:
            publication_number = ''
        redis_conn.hset('VIN_PublicationNumber_Relation', vin, publication_number)
    except Exception as e:
        print type(e), e


def set_Local_Platform_List(local_platform):  # noqa
    from django.forms.models import model_to_dict
    redis_conn = get_redis_pool()
    try:
        data = model_to_dict(local_platform)
        del data['province']
        del data['city']
        id = data.pop('id')
        redis_conn.hset('Local_Platform_List', id, json.dumps(data, ensure_ascii=False))
    except Exception as e:
        print type(e), e


def set_VIN_Local_Platform_ID_List(truck):  # noqa
    from owl import models
    redis_conn = get_redis_pool()
    vin = truck.vin
    try:
        city = truck.city
        local_platform = models.LocalPlatform.objects.filter(city=city).first()
        if not local_platform:
            province = truck.province
            local_platform = models.LocalPlatform.objects.filter(
                province=province, city=None).first()
        if local_platform:
            redis_conn.hset('VIN_Local_Platform_ID_List', vin, local_platform.id)
        else:
            redis_conn.hdel('VIN_Local_Platform_ID_List', vin)
    except Exception as e:
        print type(e), e


def set_Fault_Source_Model_Fault_Relation(key, fault, old_key=None):  # noqa
    from django.forms.models import model_to_dict
    redis_conn = get_redis_pool()
    try:
        if old_key:
            redis_conn.hdel('Fault_Source_Model_Fault_Relation', old_key)
        data = model_to_dict(fault)
        del data['description']
        del data['suggested_solution']
        redis_conn.hset('Fault_Source_Model_Fault_Relation', key, json.dumps(data, ensure_ascii=False))
    except Exception as e:
        print type(e), e


def set_VIN_FaultSourceModel_Relation(truck):  # noqa
    redis_conn = get_redis_pool()
    data = truck.source_models_dict
    redis_conn.hset('VIN_FaultSourceModel_Relation', truck.vin, json.dumps(data, ensure_ascii=False))
    return data


def set_VIN_Battery_Fault_Code_List(vin, data):  # noqa
    redis_conn = get_redis_pool()
    try:
        redis_conn.hset('VIN_Battery_Fault_Code_List', vin, json.dumps(data, ensure_ascii=False))
    except Exception as e:
        print type(e), e


def set_VIN_Motor_Fault_Code_List(vin, data):  # noqa
    redis_conn = get_redis_pool()
    try:
        redis_conn.hset('VIN_Motor_Fault_Code_List', vin, json.dumps(data, ensure_ascii=False))
    except Exception as e:
        print type(e), e


def set_VIN_Engine_Fault_Code_List(vin, data):  # noqa
    redis_conn = get_redis_pool()
    try:
        redis_conn.hset('VIN_Engine_Fault_Code_List', vin, json.dumps(data, ensure_ascii=False))
    except Exception as e:
        print type(e), e


def inc_alert_level(alert_level):
    redis_conn = get_redis_pool()
    redis_conn.hincrby('Alert_Counters', 'alert_level_%s' % alert_level, 1)


def dec_alert_level(alert_level):
    redis_conn = get_redis_pool()
    redis_conn.hincrby('Alert_Counters', 'alert_level_%s' % alert_level, -1)


redis_conn = get_redis_pool()

if __name__ == '__main__':
    pass
