from bunch import Bunch

from utils.type_convert import bytes_to_int
from time_utils import parse_to_datetime, get_now
from conf.constants import COMMAND_TYPE, BIND_ACTION, LOCK_ACTION


def do_parse_data(data):
    """
    Deconstruct the orgin package and it's payload

    pre: data passed checksum

    :data: Orginal data content
    :returns: A package dict

    """
    package = deconstruct_package(data)
    package.payload_raw = package.payload
    package.payload = deconstruct_payload(package.command_flag, package.payload)
    return package


def deconstruct_package(data):
    """
    Deconsturct a package, return a dict

    :param data: package conent
    :type data: str
    :rtype: dict
    """
    package = Bunch()
    package.start = data[0:2]
    package.command_flag = bytes_to_int(data[2])
    package.answer_flag = bytes_to_int(data[3])
    package.unique_code = data[4:21]
    package.encrypto_method = data[21]
    package.length = bytes_to_int(data[22:24])
    package.payload = data[24:-1]
    package.checksum = bytes_to_int(data[-1])
    return package


def deconstruct_payload(command_flag, data):
    """
    Deconstruct payload content for different command flag

    :command_flag: the command type
    :data:         payload content
    :returns:      a payload dict

    """
    if command_flag == COMMAND_TYPE.LOGIN:
        return deconstruct_login_payload(data)

    elif command_flag == COMMAND_TYPE.REALTIME_STATUS:
        return deconstruct_status_payload(data)

    elif command_flag == COMMAND_TYPE.REISSUE_DATA:
        return deconstruct_status_payload(data)

    elif command_flag == COMMAND_TYPE.LOGOUT:
        return deconstruct_logout_payload(data)

    elif command_flag == COMMAND_TYPE.CONTROL_COMMAND:
        payload = Bunch()
        payload.timestamp = parse_to_datetime(data)
        return payload

    elif command_flag == COMMAND_TYPE.UPSTREAM_STREAM:
        return deconstruct_report_payload(data)


def deconstruct_bind_payload(data):
    payload = Bunch()
    payload.time = data[:6]
    payload.command_id = bytes_to_int(data[6])
    payload.iccid = data[7:27]
    payload.device_id = data[27:31]
    payload.vin = data[31:48]
    payload.platform_id = data[48:68]
    payload.ecu_type = data[68:70]
    return payload


def deconstruct_lock_payload(data):
    payload = Bunch()
    payload.time = data[:6]
    payload.command_id = bytes_to_int(data[6])
    payload.iccid = data[7:27]
    payload.device_id = data[27:31]
    payload.vin = data[31:48]
    payload.platform_id = data[48:68]
    payload.rotate_speed = bytes_to_int(data[68:70])
    payload.torque = bytes_to_int(data[70])
    return payload


def deconstruct_report_bind_payload(data):
    payload = Bunch()
    payload.time = data[:6]
    payload.command_id = bytes_to_int(data[6])
    payload.iccid = data[7:27]
    payload.device_id = data[27:31]
    payload.vin = data[31:48]
    payload.platform_id = data[48:68]
    payload.current_state = bytes_to_int(data[68])
    payload.execute_state = bytes_to_int(data[69])
    payload.failure_reason = bytes_to_int(data[70])
    return payload


def deconstruct_login_payload(data):
    pass


def deconstruct_status_payload(data):
    pass


def deconstruct_logout_payload(data):
    pass


def deconstruct_report_payload(data):
    """
    Parse bind and lock conmmand reply upstream payload
    """

    payload = Bunch()
    payload.obd_time = parse_to_datetime(data[:6])
    payload.command_id = bytes_to_int(data[6])
    payload.iccid = data[7:27]
    payload.obd_id = data[27:31].encode('hex')
    payload.vin = data[31:48]
    payload.platform_id = data[48:68]
    payload.receive_time = get_now()
    if payload.command_id in BIND_ACTION.values():
        # Bind
        payload.ecu_type = data[68:70]
        payload.current_state = bytes_to_int(data[70])
        payload.execute_state = bytes_to_int(data[71])
        payload.failure_reason = bytes_to_int(data[72])
    elif payload.command_id in LOCK_ACTION.values():
        # Lock
        payload.current_state = bytes_to_int(data[68])
        payload.execute_state = bytes_to_int(data[69])
        payload.failure_reason = bytes_to_int(data[70])
    return payload
