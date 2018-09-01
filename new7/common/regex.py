# coding: utf-8

import re

RE_PHONE = re.compile(r'^(\d{5}|\d{3,4}(|-)\d{3,4}(|-)\d{3,4})$')


def error_phone(phone):
    return False if RE_PHONE.match(phone) else True
