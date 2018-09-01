# coding=utf-8

import jwt
import requests
import json
import time
from conf import config
from utils.common_utils import auth_key


def login(username, password):
    data = {
        'key': auth_key(),
        'mobile': username,
        'password': password
    }
    headers = {
        'Content-Type': 'application/json'
    }
    request = requests.post(
        '%sapi/accounts/login/' % config.SSO_URL,
        data=json.dumps(data),
        headers=headers
    )
    try:
        request_data = request.json()
    except Exception:
        return None
    if request_data.get('token'):
        try:
            user = jwt.decode(
                request_data['token'], config.SSO_SECRET_KEY, 'HS512'
            )
        except Exception:
            return None
        return user
    else:
        return None


def token_decode(token):
    try:
        user = jwt.decode(token, config.SSO_SECRET_KEY, 'HS512')
    except Exception:
        return None
    if user['exp'] < time.time():
        return None
    return user

if __name__ == '__main__':
    print login('18323177363', '123456')
    print token_decode('eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjE1OTAwMDA5OTk5IiwibW9iaWxlIjoiMTU5MDAwMDk5OTkiLCJ1c2VyX2lkIjoyMTEsImVtYWlsIjoiIiwiZXhwIjoxNDY0ODU3MzY2fQ.ibfY4P5SiNjGHJdCHZGAIbjVPCUqFaPet9s3K1FB3aq0Z13G0JNK2DJ5ASgIRuCAy-HOUrcm9oyfgswMVVYRsQ')  # noqa
