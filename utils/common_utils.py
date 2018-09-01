#!/usr/bin/env python
# coding=utf-8

import sys
import rsa
import json
import time
import ssl
import random
import string
import socket
import base64
import hashlib
import binascii
import shortuuid
from datetime import (
    date,
    datetime,
    timedelta,
)
from munch import Munch

from . import defines
from utils import regex


class DictObject(Munch):
    @property
    def _data(self):
        return self

    def __getattr__(self, k):
        try:
            return object.__getattribute__(self, k)
        except AttributeError:
            try:
                return self[k]
            except KeyError:
                return None


def auth_key():
    from conf import config
    return hashlib.sha1(
        config.KEY + time.strftime("%Y%m%d%H", time.localtime())
    ).hexdigest()


def is_testing():
    if (len(sys.argv) > 1 and sys.argv[1] == 'test'):
        return True
    return False


def get_uuid(length=10, letters_only=False):
    alphabet = None
    if letters_only:
        alphabet = list(string.letters)
    return shortuuid.ShortUUID(alphabet).random(length=length)


def get_now():
    return datetime.now()


def parse_datetime(datetime_str, fmt=defines.COMMON_TIME_STRING):
    return datetime.strptime(datetime_str, fmt)


def to_timestamp(dt):
    if isinstance(dt, str):
        dt = parse_datetime(dt)
    return int(time.mktime(dt.timetuple()))


def get_date_or_datetime(datetime_str, formats=None):
    default_formats = [
        '%Y-%m-%d',
    ]
    if formats:
        default_formats.append(formats)

    for datetime_format in default_formats:
        try:
            datetime_value = datetime.strptime(
                datetime_str, datetime_format
            )
            return datetime_value
        except (ValueError, TypeError):
            continue
    return None


def format_time(t):
    if t:
        return t.strftime('%H:%M')
    return ''


def format_date(d):
    return d.strftime(defines.COMMON_DATE_STRING)


def format_datetime(dt, fmt=defines.COMMON_TIME_STRING):
    return dt.strftime(fmt)


def dict_has_subset(more, less):
    for k, v in less.iteritems():
        if k not in more:
            return False
        if more[k] != v:
            return False
    return True


def get_error_msg(form):
    label = u'错误'
    try:
        label = form.fields[form.errors.items()[0][0]].label or label
    except:
        pass
    msg = u'{0}: {1}'.format(
        label,
        form.errors.values()[0][0]
    )
    return msg


def time_delta_display(time_delta, no_time_display=u'刚刚'):
    if time_delta.days:
        days = time_delta.days
        if days / 365:
            year = days / 365
            result = u'%d年' % year
        elif days / 31:
            month = days / 31
            result = u'%d个月' % month
        else:
            result = u'%d天' % days
    elif time_delta.seconds:
        seconds = time_delta.seconds
        if seconds / 3600:
            hours = seconds / 3600
            result = u'%d小时' % hours
        elif seconds / 60:
            minutes = seconds / 60
            result = u'%d分钟' % minutes
        else:
            result = u'%d秒' % seconds
    else:
        result = no_time_display
    return result


def delete_commercial(instance):
    dealer_list = instance.dealer_set.all()
    for dealer in dealer_list:
        # 经销商和商务处多对多，如果经销商没有商务处了，则删除这个经销商
        if len(dealer.commercial.all()) == 1:
            dealer.deleted = True
        dealer.save()
    instance.deleted = True
    instance.save()


def contract_repayment_count(start_time, repayment_count):
    """
    计算还款期数还剩多少期
    """
    now = datetime.now()
    if isinstance(start_time, str):
        start_time = datetime.datetime.strptime(
            start_time, '%Y-%m-%d'
        )
    years = now.year - start_time.year
    months = now.month - start_time.month
    months += years * 12
    days = now.day - start_time.day
    if days < 0:
        months -= 1
    delta = repayment_count - months
    if delta < 0:
        delta = 0
    return delta


def add_spider_header(request_session):
    request_session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-encoding": "gzip,deflate,sdch",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    })


def encrypt(secret):
    pubkey = rsa.PublicKey.load_pkcs1(defines.PUBKEY)
    encrypted = rsa.encrypt(secret, pubkey)
    return base64.b64encode(encrypted)


def decrypt(b64string):
    encrypted = base64.b64decode(b64string)
    privkey = rsa.PrivateKey.load_pkcs1(defines.PRIVKEY)
    decrypted = rsa.decrypt(encrypted, privkey)
    return decrypted


def get_socket(host, port, timeout=0):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if timeout:
        my_socket.settimeout(timeout)
    my_socket.connect((host, port))
    return my_socket


def get_ssl_socket(host, port=443):
    """
    PROTOCOL_SSLv2
    PROTOCOL_SSLv3
    PROTOCOL_SSLv23
    PROTOCOL_TLSv1
    PROTOCOL_TLSv1_1
    PROTOCOL_TLSv1_2
    """
    sslprotocol = ssl.PROTOCOL_TLSv1
    # 安全ssl
    # context = ssl.SSLContext(sslprotocol)
    # context.verify_mode = ssl.CERT_REQUIRED
    # context.load_default_certs()
    # 自签名
    context = ssl._create_unverified_context(sslprotocol)
    context.load_default_certs()
    # context.load_cert_chain('../ssl_cert/server.pem')

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(my_socket)
    ssl_sock.connect((host, port))
    ssl_sock.setblocking(0)
    return ssl_sock


def convert_to_string(value):
    if isinstance(value, unicode):
        return value.encode('utf-8')
    if isinstance(value, (list, tuple, dict)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def weixin_sign(jsapi_ticket, url):
    now = get_now()
    timestamp = now.strftime('%s')
    noncestr = ''.join(random.sample(string.ascii_letters, 16))
    sign_string = 'jsapi_ticket=%s&noncestr=%s&timestamp=%s&url=%s' % (
        jsapi_ticket,
        noncestr,
        timestamp,
        url,
    )
    signature = hashlib.sha1(sign_string).hexdigest()
    return {
        'timestamp': timestamp,
        'noncestr': noncestr,
        'signature': signature,
    }


def to_date(date_string, fmt='%Y%m%d'):
    return datetime.strptime(date_string, fmt).date()


def is_id_num_checked(id_num):
    if not regex.RE_IDENTITY.match(id_num):
        return False
    if id_num[:2] not in defines.AREA_CODES:
        return False
    birthday = id_num[6:14]
    try:
        birthday = to_date(birthday)
    except ValueError:
        return False
    today = date.today()
    if birthday > today:
        return False
    if today.year - birthday.year > 150:
        return False
    check_sum = 0
    for i in range(17):
        check_sum = check_sum + int(id_num[i]) * defines.ID_WEIGHT[i]
    check_bit = check_sum % 11
    if id_num[-1].upper() != defines.ID_CHECK[check_bit]:
        return False
    return True


def hex_to_char(one):
    # '0x61' -> 'a'
    # '0x1' -> '\x01'
    # '0x01' -> '\x01'
    return chr(int(one, 16))


def char_to_hex(one):
    # 'a' -> '0x61'
    # '\x01' -> '0x1'
    return hex(ord(one))


hexlify = binascii.hexlify  # '\x61' -> '61', '\x01' -> '01'


def split_by_length(data, length=4):
    ret = []
    while data:
        ret.append(data[:length])
        data = data[length:]
    return ret


def is_unicode_or_string_equal(a, b, encoding='utf8'):
    if type(a) is type(b):
        return a == b
    if isinstance(a, unicode):
        u = a
        s = b
    else:
        u = b
        s = a
    return u.encode(encoding) == s


def get_signed_location(data, update=True, return_type=None):
    lng = data.get('lng')
    lat = data.get('lat')
    south_or_north = data.get('south_or_north', '')
    if is_unicode_or_string_equal(south_or_north, u'南纬'):
        if isinstance(lat, float):
            lat = -lat
        else:
            lat = '-' + lat
    east_or_west = data.get('east_or_west', '')
    if is_unicode_or_string_equal(east_or_west, u'西经'):
        if isinstance(lat, float):
            lng = -lng
        else:
            lng = '-' + lng
    if update:
        data.update(lat=lat, lng=lng)
    if return_type:
        location_dict = {
            'lng': return_type(lng),
            'lat': return_type(lat),
        }
    else:
        location_dict = {
            'lng': lng,
            'lat': lat,
        }
    return location_dict


def generate_time_series(minutes_ago, interval_seconds):
    now = get_now()
    i = 0
    while True:
        t = now - timedelta(minutes=minutes_ago) + i * timedelta(seconds=interval_seconds)
        i += 1
        if t < now:
            yield t
        else:
            break


if __name__ == '__main__':
    pass
