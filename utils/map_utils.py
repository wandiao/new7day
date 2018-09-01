#!/usr/bin/env python
# coding=utf-8

import requests
import eviltransform
from munch import Munch

from conf import config

gd_key = {'key': 'ee3075f1c194c127ea1ebefbb86c76a5'}
bd_ak = {'ak': config.BAIDU_MAP_KEY}
gd_url = 'http://restapi.amap.com/v3/geocode/regeo'
bd_url = 'http://api.map.baidu.com/geocoder/v2/'
gdc_url = 'http://restapi.amap.com/v3/assistant/coordinate/convert?key=%s'
bdc_url = 'http://api.map.baidu.com/geoconv/v1/'


def gaode_location_transform(lng, lat):
    """高德经纬度转换 gps -> gcj02"""
    params = {'coordsys': 'gps'}
    locations = '%s,%s' % (lng, lat)
    params.update(locations=locations)
    resp = requests.get(gdc_url % gd_key['key'], params=params)
    result = resp.json()
    lng, lat = result["locations"].split(',')
    return lng, lat


def baidu_location_transform(lng, lat):
    resp = requests.get(
        config.BAIDU_ENCODE_URL,
        params={
            "coords": "%s,%s" % (lng, lat),
            "from": 1,
            "to": 5,
            "ak": config.BAIDU_MAP_KEY,
        }
    )
    result = resp.json()
    x = result["result"][0]["x"]
    y = result["result"][0]["y"]
    return x, y


def get_location_string(url, lng, lat):
    if url == gd_url:
        return '{0},{1}'.format(lng, lat)
    elif url == bd_url:
        return '{0},{1}'.format(lat, lng)


def regeo(url, lng='', lat='', location=None):
    """
    逆地理编码
    坐标转换成地址
    """
    params = {'output': 'json'}
    lng = str(lng or location['lng'])
    lat = str(lat or location['lat'])
    location = {'location': get_location_string(url=url, lng=lng, lat=lat)}
    params.update(location)
    if url == gd_url:
        params.update(gd_key)
        response = requests.get(url, params=params).json()
        if response['status'] == '1':
            result = response['regeocode']['formatted_address']
        else:
            result = ''
    elif url == bd_url:
        params.update(bd_ak)
        params.update(coordtype='wgs84ll')  # GPS经纬度
        response = requests.get(url, params=params).json()
        if response['status'] == 0:
            result = response['result']['formatted_address']
        else:
            result = ''
    return result


def baidu_regeo(lng='', lat='', location=None):
    return regeo(bd_url, lng, lat, location)


def gaode_regeo(lng='', lat='', location=None):
    return regeo(gd_url, lng, lat, location)


def gps2gd(data):
    location = Munch(data)
    lat, lng = map(float, [location.lat, location.lng])
    gd_lat, gd_lng = eviltransform.wgs2gcj(lat, lng)
    data.update(gd_lat=gd_lat, gd_lng=gd_lng)


def test():
    location = Munch({'lng': 116.481499, 'lat': 39.990475})  # 北京市朝阳区望京东路
    location = Munch({'lng': 111.803716, 'lat': 37.152444})  # 山西省吕梁市孝义市振兴街
    print location
    gps2gd(location)
    print location
    gcj02_lng, gcj02_lat = gaode_location_transform(location.lng, location.lat)
    print gcj02_lat[:-2], gcj02_lng[:-3]
    print baidu_regeo(location=location)
    print gaode_regeo(lng=gcj02_lng, lat=gcj02_lat)


if __name__ == '__main__':
    test()
    pass
