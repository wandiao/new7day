#!/usr/bin/env python
# coding=utf-8
from munch import Munch

COMMON_TIME_STRING = "%Y-%m-%d %H:%M:%S"
FRONT_TIME_STRING = "%Y-%m-%d %H:%M"
COMMON_DATE_STRING = "%Y-%m-%d"
YEAR_MONTH_STRING = "%Y-%m"
FILENAME_TIME_STRING = "%Y%m%d%H%M%S"

vin = 'LGHB2V190FC200001'
iccid = '89860615010032186386'

AREA_CODE_LIST = [
    ("11", u"北京"),
    ("12", u"天津"),
    ("13", u"河北"),
    ("14", u"山西"),
    ("15", u"内蒙古"),
    ("21", u"辽宁"),
    ("22", u"吉林"),
    ("23", u"黑龙江"),
    ("31", u"上海"),
    ("32", u"江苏"),
    ("33", u"浙江"),
    ("34", u"安徽"),
    ("35", u"福建"),
    ("36", u"江西"),
    ("37", u"山东"),
    ("41", u"河南"),
    ("42", u"湖北"),
    ("43", u"湖南"),
    ("44", u"广东"),
    ("45", u"广西"),
    ("46", u"海南"),
    ("50", u"重庆"),
    ("51", u"四川"),
    ("52", u"贵州"),
    ("53", u"云南"),
    ("54", u"西藏"),
    ("61", u"陕西"),
    ("62", u"甘肃"),
    ("63", u"青海"),
    ("64", u"宁夏"),
    ("65", u"新疆"),
    ("71", u"台湾"),
    ("81", u"香港"),
    ("82", u"澳门"),
    ("91", u"国外"),
]
AREA_CODES = [one[0] for one in AREA_CODE_LIST]
ID_WEIGHT = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
ID_CHECK = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

# 数据报文类型
ORDER_TYPE = {
    0x01: u'车辆登入',
    0x02: u'实时信息上报',
    0x03: u'补发信息上报',
    0x04: u'车辆登出',
    0x05: u'平台登入',
    0x06: u'平台登出',
    0x82: u'控制命令',
    0x09: u'控制命令结果上报',
}

# 应答标志
RECEIVE_TYPE = {
    0x01: u'成功',
    0x02: u'错误',
    0x03: u'VIN重复',
    0xfe: u'命令',
}

# 车辆报警按位与定义
WARNING_STATE = {
    # 字节1
    0x01: u'撞车',
    0x02: u'断电',
    0x04: u'断油',
    0x08: u'主电源断开',
    0x10: u'驶出电子围栏',
    0x20: u'驶入电子围栏',
    0x40: u'超速',
    0x80: u'紧急情况',

    # 字节2
    0x0100: u'拖吊',
    0x0200: u'怠速',
    0x0400: u'疲劳驾驶',
    0x0800: u'喇叭',
    0x1000: u'信息申请',
    0x2000: u'急救',
    0x4000: u'故障',
    0x8000: u'低压',

    # 字节3
    0x010000: u'点火',
    0x020000: u'震动',
    0x040000: u'开门',
    0x080000: u'非点火',
    0x100000: u'偷油',
    0x200000: u'低温',
    0x400000: u'高温',
    0x800000: u'禁止行驶',

    # 字节4
    0x01000000: u'停车超时',
    0x02000000: u'气体泄漏',
    0x04000000: u'欠费',
    0x08000000: u'偷盗',
}


# 车辆状态按位与定义
CAR_STATE = {
    # 字节1
    0x01: u'车辆撤防',
    0x02: u'油路正常',
    0x04: u'任务结束',
    0x08: u'震动',
    0x10: u'任务中',
    0x20: u'门开',
    0x40: u'任务启动',
    0x80: u'引擎启动',

    # 字节2
    0x0100: u'油量检测器异常',
    0x0200: u'加油',
    0x0400: u'重车',
    0x0800: u'车门上锁',
    0x1000: u'车辆设防',
    0x2000: u'出租车计价器',
    0x4000: u'引擎关到开跳变',
    0x8000: u'车辆启动时速度跳变',

    # 字节3
    0x010000: u'下坠',
    0x020000: u'翻滚',
    0x040000: u'位移',
    0x080000: u'绝对禁止',
    0x100000: u'轮胎缓慢泄气',
    0x200000: u'胎压低',
    0x400000: u'胎压高',
    0x800000: u'胎温高',

    # 字节4
    0x01000000: u'设备搭车',
    0x02000000: u'设备快跑',
    0x04000000: u'设备慢跑',
    0x08000000: u'设备散步',
}

ENCRYPTO_METHODS = {
    0x01: u'不加密',
    0x02: u'RSA',
    0x03: u'AES128',
    0xFE: u'异常',
    0xFF: u'无效',
}

ALERT_LEVEL_DICT = {
    '\x00': u'无故障',
    '\x01': u'1 级故障',
    '\x02': u'2 级故障',
    '\x03': u'3 级故障',
    '\xfe': u'异常',
    '\xff': u'无效',
}
ALERT_LEVELS = [
    '\x00',
    '\x01',
    '\x02',
    '\x03',
    '\xfe',
    '\xff',
]

CAR_STATUSES = (
    ('\x01', u'启动'),  # 'started'
    ('\x02', u'熄火'),  # 'stopped'
    ('\x03', u'其他'),  # 'other'
    ('\xfe', u'异常'),  # 'abnormal'
    ('\xff', u'无效'),  # 'invalid'
)
OBD_CAR_STATUS_DICT = dict(CAR_STATUSES)
CAR_STATUSES_CHOICES = ((cn, cn) for _, cn in CAR_STATUSES)

TRUCK_TYPE = {
    'traditional': u'传统能源车辆',
    'new_energy': u'新能源车辆',
}

MONITOR_TYPE_META = {
    'speed': u'速度',
    'rev': u'转速',
    'water_temperature': u'水温',
    'voltage': u'电压',
}

METHOD_META = {
    'gt': u'超过',
    'eq': u'达到',
    'lt': u'低于',
}

RANK_CHOICES = (
    ('platform_company', u'总平台公司'),
    ('main_factory', u'主机厂'),  # 板块
    ('division', u'事业部'),  # 营业部
    ('commercial', u'商务处'),
    ('dealer', u'经销商'),
    ('major', u'大客户'),
)
ROLE_CHOICES = (
    ('super_admin', u'超级管理员'),
    ('admin', u'管理员'),
    ('native', u'地方平台管理员'),
)
RANK_ROLE_RESTRICTION = {
    'platform_company': [
        'super_admin',
        'admin',
        'worker',
        'warekeeper',
    ],
    'main_factory': [
        'super_admin',
        'admin',
        'worker',
    ],
    'division': [
        'super_admin',
        'admin',
        'worker',
    ],
    'commercial': [
        'super_admin',
        'admin',
        'worker',
    ],
    'dealer': [
        'super_admin',
        'admin',
        'worker',
        'warekeeper',
    ],
    'major': [
        'super_admin',
        'admin',
        'worker',
    ],
}

NationalStandardAlertInfo = (
    ('temperature_difference_alert', u'温度差异报警', '0000000001'),
    ('battery_high_temperature_alert', u'电池高温报警', '0000000002'),
    ('energy_storage_device_high_voltage_alert', u'车载储能装置过压报警', '0000000003'),
    ('energy_storage_device_low_voltage_alert', u'车载储能装置欠压报警', '0000000004'),
    ('soc_low_alert', u'SOC 低报警', '0000000005'),
    ('single_battery_high_voltage_alert', u'单体电池过压报警', '0000000006'),
    ('single_battery_low_voltage_alert', u'单体电池欠压报警', '0000000007'),
    ('soc_too_high_alert', u'SOC 过高报警', '0000000008'),
    ('soc_jumping_alert', u'SOC 跳变报警', '0000000009'),
    ('rechargeable_energy_storage_system_mismatch_alert', u'可充电储能系统不匹配报警', '0000000010'),
    ('battery_cell_consistency_low_alert', u'电池单体一致性差报警', '0000000011'),
    ('insulation_alert', u'绝缘报警', '0000000012'),
    ('dc_dc_temperature_alert', u'DC-DC 温度报警', '0000000013'),
    ('braking_system_alert', u'制动系统报警', '0000000014'),
    ('dc_dc_status_alert', u'DC-DC 状态报警', '0000000015'),
    ('motor_controller_temperature_alert', u'驱动电机控制器温度报警', '0000000016'),
    ('hvil_alert', u'高压互锁状态报警', '0000000017'),
    ('motor_temperature_alert', u'驱动电机温度报警', '0000000018'),
    ('energy_storage_device_over_charge_alert', u'车载储能装置类型过充', '0000000019'),
    ('low_electricity', u'低电报警', '0000000020'),
    ('main_power_down', u'主电源断电报警', '0000000021'),
    ('CAN_communication_fault', u'CAN 通信故障', '0000000022'),
    ('positioning_antenna_cut', u'定位天线断开', '0000000023'),
    ('positioning_antenna_short_circuit', u'定位天线短路', '0000000024'),
    ('gps_antenna_cut_down', u'GPS天线剪短报警', '0000000025'),
)
AlertInfo = NationalStandardAlertInfo
AlertTypes = [one[0] for one in AlertInfo]
ExtendAlertTypes = [one[0] for one in AlertInfo[19:]]
CustomAlertTypes = ['main_power_down', 'device_offline', 'mileage_lt']
AlertChoices = (
    (one[0], one[1]) for one in AlertInfo
)
AlertTypeCodeDict = {
    one[0]: one[2] for one in AlertInfo
}
AlertTypeNameDict = {
    one[0]: one[1] for one in AlertInfo
}
default_alert_level = '3'
DEFAULT_ALERT_LEVEL_SETTINGS = {
    one[0]: default_alert_level for one in AlertInfo
}

TRUCK_KEY_MAP = {
    u'车牌号': 'truck_number',
    u'VIN': 'vin',
    u'发动机编号': 'engine_number',
    u'车载终端编号': 'obd_id',
    u'车辆生产商': 'main_factory',
    u'车系': 'truck_serie',
    u'车型': 'truck_model',
    u'SIM': 'sim_id',
    u'SIM卡ICCID号': 'iccid',
    u'服务费到期时间': 'service_fee_due_time',
    u'年审时间': 'yearly_check_time',
    u'保险到期时间': 'insurance_due_time',
    u'备注': 'remarks',
    u'车辆用途': 'truck_usage',
    u'车辆生产日期': 'truck_made_date',
    u'销售日期': 'sale_date',
    u'可充电储能系统编码': 'rechargeable_energy_storage_system_encoding',
    u'动力蓄电池生产日期': 'power_battery_made_date',
    u'驱动电机序号': 'motor_serial_number',
    u'接入日期': 'join_up_date',
    u'上线日期': 'put_online_date',
    u'运营单位': 'operation_unit',
    u'存放地点': 'storage_address',
    u'联系人': 'contact_name',
    u'联系电话': 'contact_phone',
    u'车企唯一标识': 'truck_company_id',
    u'行驶证号': 'vehicle_license_number',
    u'购车人居住地所在区县': 'buyer_residential_county_name',
    u'单位法人代表': 'legal_representative_name',
    u'法人代表手机': 'legal_representative_phone',
    u'运营单位地址': 'operation_unit_address',
    u'运营地址': 'operate_address',
    u'对应车辆充电桩地址': 'charging_pile_address',
    u'车牌颜色': 'plate_color',
    u'车辆开票时间': 'truck_invoice_time',
    u'车辆上牌时间': 'register_plate_date',
    u'国补补贴金额': 'national_subsidy_amount',
    u'申报公示时间': 'report_publicity_time',
    u'车辆运营属性': 'operate_nature',
    u'所属机构名称': 'affiliated_org_name',
    u'上牌单位': 'licensing_department',
    u'开票金额': 'invoice_amount',
    u'发票号': 'invoice_number',
    u'地方平台归属': 'local_platform',
}
TRUCK_EXPORT_MAP = TRUCK_KEY_MAP.copy()
TRUCK_EXPORT_MAP.update({
    u'车系名称': 'truck_serie_name',
    u'车型': 'publication_number',
    u'车辆生产商': 'main_factory_name',
    u'地方平台名称': 'local_platform_name',
    u'车辆类别名称': 'truck_category_name',
    u'事业部名称': 'division_name',
    u'商务处名称': 'commercial_name',
    u'经销商名称': 'dealer_name',
    u'客户名称': 'client_name',
    u'终端厂商': 'device_maker',
    u'车辆用途': 'truck_usage',
    u'发票号': 'invoice_number',
    u'金融类型': 'financial_type',
    u'上牌区域': 'register_plate_region',
    u'监控起始时间': 'monitor_start_time',
    u'单位类型': 'unit_type',
    u'总负责人名字': 'chief_person_in_charge_name',
    u'总负责人电话': 'chief_person_in_charge_phone',
    u'存放点联系人名字': 'contact_name',
    u'存放点联系人电话': 'contact_phone',
    u'车辆负责人名字': 'driver_name',
    u'车辆负责人电话': 'driver_phone',
    u'车辆出厂日期': 'leave_factory_date',
    u'批次号': 'batch_number',
    u'投运日期': 'put_into_operation_date',
    u'合格证编号': 'qualification_number',
    u'发动机品牌': 'engine_model_brand_name',
    u'发动机型号': 'engine_model_name',
    u'电池品牌': 'battery_model_brand_name',
    u'电池型号': 'battery_model_name',
    u'电机品牌': 'motor_model_brand_name',
    u'电机型号': 'motor_model_name',
})
REVERSED_TRUCK_EXPORT_MAP = {
    v: k for k, v in TRUCK_EXPORT_MAP.items()
}
ALERT_LEVEL_CHOICES = (
    ('1', u'一级'),
    ('2', u'二级'),
    ('3', u'三级'),
    ('unknown', u'未知'),
)
ALERT_STATUS_CHOICES = (
    ('alerting', u'报警中'),
    ('cleared', u'已解除'),
)
VEHICLE_RUNNING_STATUS_CHOICES = (
    ('unknown', u'未知'),
    ('driving', u'行驶'),
    ('alerting', u'报警'),
    ('charging', u'充电'),
    ('stopped', u'停止'),
    ('offline', u'离线'),
    ('logged_in', u'已登入'),
    ('logged_out', u'已登出'),
)

BATTERY_TYPE_INFO = (
    ('\x01', '', u'磷酸铁锂电池'),
    ('\x02', '', u'锰酸锂电池'),
    ('\x03', '', u'钴酸锂电池'),
    ('\x04', '', u'三元材料电池'),
    ('\x05', '', u'聚合物锂离子电池'),
    ('\x06', '', u'超级电容'),
    ('\x07', '', u'钛酸锂电池'),
    ('\xFC', '', u'燃料电池'),
    ('\xFF', 'other', u'其他车载储能装置类型'),
)
MOTOR_LAYOUT_INFO = (
    ('edge', u'轮边电机'),
    ('rim', u'轮毂电机'),
    ('dual', u'前后双电机'),
    ('unknown', u'未知'),
)

TEXT_REPLY = """
<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
</xml>
"""

TEXT_IMG_REPLY = """
<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[news]]></MsgType>
    <ArticleCount>1</ArticleCount>
    <Articles>
    <item>
        <Title><![CDATA[%s]]></Title>
        <Description><![CDATA[%s]]></Description>
        <PicUrl><![CDATA[%s]]></PicUrl>
        <Url><![CDATA[%s]]></Url>
    </item>
    </Articles>
</xml>
"""

ES3_PUBKEY = """"""

PRIVKEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAqD3wmZhc98j67PRyA/WJ17AtOjkyN8xuPJTJ9NWKa9aeo4qo
AE9jMvE474pvHKCFsZF1UA+VUKd7Twz4mAIdXGzj2fwlyYlacI4dM1EqImd55KQk
hG0ekXReFhN3jkeOEAFBa2tcDV1mfml4dQn4+CcZ7LHQmZLQBrZC/UhnhT2MVVe+
9876aVh/JvL3NgoYjPVEuGdzE825VVZqNLLkSfPgIORe/94mQ6bbVQ75Ikf33nW8
4/goRGium+01NLkn0lnVskYmp5X9hdFi9uvg+qnUmfj6Q3KfbsSm3yYxywkG7aHG
GfRskllo1bcBnKe/4gkpH6Q0AG21ZVWuIsIDQwIDAQABAoIBAG+0GGBSmj9mcLwN
HPpl92x+q7jBqwcDM5oDjAeEFJC/AbtB34O9Mfbr1EqvFlDif4HDOym5/wB7AtMc
oJ2Eoevw3GOqF4i1Kpgas2aUGC6Zl4PoO9q0/JvEsIdly3ZrKfaUbtQchxTUk62Q
54qF4YkZpQvTj9W3dWlPcDDs9tauUD1trMqaZ0b4nyoZmr/h+2jmUSZvG2o0cDop
amhpvHOl45cCY5YEzuYwFqNM8HL873uni+aZhZipK4gro4BCAaauXeLWm309FeXD
1sY9MrA0FcyqgDQYhzrXLBlmnIzwIWCNX13quGMxSm++TaabovwTky+dCe9tzW8W
Nji3ajkCgYEA0A/OmTBhShkz+xtNMPgl8KeCEJ7QCZVLpgHEztwGWMGDGz7N7WD3
t7kMXWYcq8cHoH9Dc2Y0rh8fznzqAdCcFe4xqCwbO+GJCLcCa1kCC68tM3BwYA6c
gTpfa8lL5mLsB6SP07fLXgWTG5+JEcI0q4ekDNQnELEEKaISz2DubPUCgYEAzwFs
3wNXxKxGlE19KbCwEDp9I96RlSb9L9bZzyfdhLfFBz3R+HIkv4ltSSJl/6x91i7S
4tgv+czmt6XeVQDCYR4Z+OKP3F3IjORayt42T4Se8mH1ZCcry2gmANrf1L5CJ35n
V+dpJE6OAyuMwvndWhhtmTzF+1GUMd3YEx5xjFcCgYB8pvvAC5w+KJtb9h9pF0Kj
y7fA/WTmWOvZqXWf+XJT+pvx1s7JSS8gg11FF8hVogiPv69JlBI7v6nurCgGrlTV
Tr+xYbtvRNA0yHBKoCj5lxodl1+8LQTW54IDsbYncVy3t3/z+El/KxfXlN0qJpAn
tDw082X0OhmkV9WtKQWvgQKBgFcDZlwn75DASbq1B9OqbZekvk2BlPh5NxwQ1+V4
AGl1ReDRX51rfX71qXaAexeJzitl60dnUGNUefbgRiC8/PgNyyUPNyGOWmq+4ls8
JOAwAxAnlRrQTFxoHvFlD4lBoFUxkQcmQs/8JT235KdgmGbytb8gCKinlf+QHO+M
cHZpAoGBAIBMdb3cvyOT9XDH9fGIGH75bsf+yoA70Vaz6Wa4TSxNloKAI3v/oQhi
VCB7ayARY3lIKcugNa769IdZWiE0AlB4mfd24IN6a12U6WPV/xgMu6MQa1istXPN
0pqY3xAsw4rYQoPks8CROZDCR9ErYgxOg8CBgWAKxUq1NRJ+7UQA
-----END RSA PRIVATE KEY-----
"""

PUBKEY = """
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAqD3wmZhc98j67PRyA/WJ17AtOjkyN8xuPJTJ9NWKa9aeo4qoAE9j
MvE474pvHKCFsZF1UA+VUKd7Twz4mAIdXGzj2fwlyYlacI4dM1EqImd55KQkhG0e
kXReFhN3jkeOEAFBa2tcDV1mfml4dQn4+CcZ7LHQmZLQBrZC/UhnhT2MVVe+9876
aVh/JvL3NgoYjPVEuGdzE825VVZqNLLkSfPgIORe/94mQ6bbVQ75Ikf33nW84/go
RGium+01NLkn0lnVskYmp5X9hdFi9uvg+qnUmfj6Q3KfbsSm3yYxywkG7aHGGfRs
kllo1bcBnKe/4gkpH6Q0AG21ZVWuIsIDQwIDAQAB
-----END RSA PUBLIC KEY-----
"""

SHANGHAI_PUBKEY = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQChixw4y0BDtlufNiwby9UTpamp
VdduYgBmCRdwJKfY/SPe/jGIdbmq1FONZiVBYArcfkVt4sDZpQ4Qh8nmNhU1kwOX
YnehmPUVaWLo5lhd+OsGHbE+P6ZzvSG8f8R/BNK5uHSucC2mwsqG5nmfCwTLLaCn
r4uu+EahTvDqW6AhMQIDAQAB
-----END PUBLIC KEY-----
"""

shanghai_truck_fields_map = Munch({
    'publication_number': 'modelCode',  # 车型型号(备案车型)
    'shanghai_truck_usage': 'vehUse',  # 车辆用途
    'truck_made_date': 'vehMakeDate',  # 车辆生产日期
    'sale_date': 'saleDate',  # 销售日期
    'rechargeable_energy_storage_system_encoding': 'batAccuCode',  # 可充电储能系统编码
    'power_battery_made_date': 'accuMakeDate',  # 动力蓄电池生产日期
    'motor_serial_number': 'dynNo',  # 驱动电机序号
    'engine_number': 'engineNo',  # 发动机编号
    'obd_id': 'sn',  # 车载终端编号
    'join_up_date': 'inDate',  # 接入日期
    'put_online_date': 'onLineDate',  # 上线日期
    'truck_number': 'vehNo',  # 车牌号
    'operation_unit': 'motonCompany',  # 运营单位
    'storage_address': 'addr',  # 存放地点
    'contact_name': 'linkman',  # 联系人
    'contact_phone': 'linkphone',  # 联系电话
    'truck_company_id': 'veCode',  # 车企唯一标识
    'vehicle_license_number': 'drivLicenNum',  # 行驶证号
    'buyer_residential_county_name': 'buyerCarCounty',  # 购车人居住地所在区县
    'legal_representative_name': 'operatUnitLegal',  # 单位法人代表
    'legal_representative_phone': 'operatUnitLegalTel',  # 法人代表手机
    'operation_unit_address': 'operatUnitAddress',  # 运营单位地址
    'operate_address': 'operatAddress',  # 运营地址
    'charging_pile_address': 'vehChargeAddress',  # 对应车辆充电桩地址
    'device_type': 'terminalType',  # 终端类型
    'device_maker': 'terminalFirm',  # 终端厂商
})
SHANGHAI_TRUCK_URL = 'http://106.14.51.20:8080/EvdataAPI/veh/add'

shanghai_battery_fields_map = Munch({
    'battery_type': 'batteryType',  # 电池类型
    'battery_code_std_type': 'batteryCodeType',  # 电池编码标准
    'battery_manufacturer': 'batteryPackageCompany',  # 电池包生产企业
    'battery_voltage': 'batteryPackageVoltage',  # 电池包额定电压
    'battery_capacity': 'batteryPackageCapacity',  # 电池包额定容量
    'battery_code': 'batteryPackageCode',  # 电池包编码
    'battery_made_date': 'batteryPackageDate',  # 电池包生产日期
    'battery_module_voltage': 'batteryModuleVoltage',  # 电池模组额定电压
    'battery_module_capacity': 'batteryModuleCapacity',  # 电池模组额定容量
    'battery_module_code': 'batteryModuleCode',  # 电池模组编码
    'battery_cell_manufacturer': 'batteryCellCompany',  # 电芯生产企业
    'battery_cell_voltage': 'batteryCellVoltage',  # 电芯额定电压
    'battery_cell_capacity': 'batteryCellCapacity',  # 电芯额定容量
    'battery_cell_code': 'batteryCellCode',  # 电芯编码
})
SHANGHAI_BATTERY_URL = 'http://data.shevdc.org/evdata-web/api/service/batteryData/import'


if __name__ == '__main__':
    pass
