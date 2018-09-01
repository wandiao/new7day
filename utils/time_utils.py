import time
from datetime import datetime

from utils.type_convert import bytes_to_int


def unix_timestamp(time_field):
    """
    Deconstruct time field in package, return unix timestamp in int

    :type time_field: str
    :rtype: int
    """
    dt = parse_to_datetime(time_field)
    return int(time.mktime(dt.timetuple()))


def parse_to_datetime(time_field):
    """
    Convert time hexdata to datetime

    :type time_field: str
    :rtype: datetime
    """
    year = 2000 + bytes_to_int(time_field[0])
    month = bytes_to_int(time_field[1])
    day = bytes_to_int(time_field[2])
    hour = bytes_to_int(time_field[3])
    minute = bytes_to_int(time_field[4])
    second = bytes_to_int(time_field[5])

    dt = datetime(year, month, day, hour, minute, second)
    return dt


def get_now():
    dt = datetime.now()
    return dt.strftime('%Y-%m-%d %H:%M:%S')
