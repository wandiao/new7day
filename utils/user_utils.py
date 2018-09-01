# coding=utf-8

import requests
import json
from conf import config
from utils.common_utils import auth_key


def add_user(username, password, product_user_id):
    data = {
        'mobile': username,
        'password': password,
        'product_user_id': product_user_id,
        'product_id': config.PRODUCT_ID,
        'key': auth_key(),
    }
    headers = {
        'Content-Type': 'application/json'
    }
    request = requests.post(
        '%sapi/open/add_user/' % config.SSO_URL,
        data=json.dumps(data),
        headers=headers
    )

    try:
        request_data = request.json()
    except Exception:
        return False
    if request_data.get('status') == 'success':
        return True
    elif request_data.get('status') == 'error':
        return request_data['msg']
    else:
        return False


def reset_password(username, password):
    data = {
        'mobile': username,
        'password': password,
        'key': auth_key(),
    }
    headers = {
        'Content-Type': 'application/json'
    }
    request = requests.post(
        '%sapi/open/reset_password/' % config.SSO_URL,
        data=json.dumps(data),
        headers=headers
    )

    try:
        request_data = request.json()
    except Exception:
        return False
    if request_data.get('status') == 'success':
        return True
    elif request_data.get('status') == 'error':
        return request_data['msg']
    else:
        return False


if __name__ == '__main__':
    # print reset_password('18900000019', '18900000010')
    # print add_user('18900000019', '18900000019')
    pass
