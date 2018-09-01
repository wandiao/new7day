import struct


def bytes_to_int(byte, byte_order='>'):
    """
    :type byte: str
    :type byte_order: str
    """
    if len(byte) == 1:
        format_flag = 'B'
    elif len(byte) == 2:
        format_flag = 'H'
    elif len(byte) == 4:
        format_flag = 'L'

    format_string = byte_order + format_flag

    return struct.unpack(format_string, byte)[0]


def int_to_bytes(integer, bytes_size=4, byte_order='>'):
    """
    :type byte: str
    :type byte_order: str
    """
    if bytes_size == 1:
        format_flag = 'B'
    elif bytes_size == 2:
        format_flag = 'H'
    elif bytes_size == 4:
        format_flag = 'L'

    format_string = byte_order + format_flag

    return struct.pack(format_string, integer)
