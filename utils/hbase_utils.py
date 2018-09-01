#!/usr/bin/env python
# -*- coding: utf-8 -*-

import happybase
import random


from conf import config
from utils import common_utils

hosts = config.THRIFT_HOSTS
port = config.THRIFT_PORT


def get_connection():
    host = random.choice(hosts)
    connection = happybase.Connection(host=host, port=port)
    return connection


def create_table(connection, table_name, column_families):
    if config.COMPRESS_HBASE:
        desc = {
            cf: dict(compression='snappy') for cf in column_families
        }
    else:
        desc = {
            cf: dict() for cf in column_families
        }
    connection.create_table(
        table_name,
        desc,
    )


def delete_table(connection, table_name):
    return connection.delete_table(table_name, disable=True)


def get_table(connection, table_name):
    if not connection:
        connection = get_connection()
    table = connection.table(table_name)
    return table


def construct_data(data_structure, original_data):
    data = {}
    for cf, columns in data_structure.iteritems():
        for raw, col in columns.iteritems():
            value = original_data.get(raw)
            if value is not None:
                key = u'%s:%s' % (cf, col)
                data[key] = common_utils.convert_to_string(value)
    return data


def save_to_hbase(table_name, row_key, data):
    pass


if __name__ == '__main__':
    pass
