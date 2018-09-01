#!/usr/bin/env python
# encoding: utf-8
import random
from conf.config import SMS_TIMEOUT


def generate_sms_code(count=6):
    """生成指定位数短信验证码"""
    if not isinstance(count, int) or count < 1:
        count = 6
    start = 10**(count - 1)
    end = 10**count - 1
    return random.randint(start, end)


def set_sms_code_cache(phone, code, cache):
    """短信验证码写cache"""
    r_key = 'v_code_%s' % phone
    cache.set(r_key, code, timeout=SMS_TIMEOUT)


def validate_sms_code(phone, code, cache):
    """短信验证码校验"""
    if not code:
        return False
    try:
        code = int(code)
    except ValueError:
        return False
    r_key = 'v_code_%s' % phone
    true_code = cache.get(r_key)
    if not true_code:
        return False
    if true_code == code:
        return True
    else:
        return False
