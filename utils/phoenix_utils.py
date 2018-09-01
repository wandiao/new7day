# coding=utf-8

import logging
import logging.config
import phoenixdb

from conf import config

logging.config.fileConfig(config.LOG_CONFIG_LOCATION)
logger = logging.getLogger(__name__)


def get_cursor():
    connection = phoenixdb.connect(config.PHOENIX_QUERY_SERVER, readonly=False,
                                   autocommit=True)
    cursor = connection.cursor()
    return cursor


def query_all(cursor, view_name):
    try:
        cursor.execute("""select * from "%s" """ % view_name)
        logger.debug(cursor.fetchall())
        cursor.close()
    except Exception as e:
        logger.error("query view error, the error info is %s " % e)
        raise e


def create_view(cursor, view_name, columns_name):
    try:
        command = """create view if not exists "%s" ( """ % view_name
        for cf, columns in columns_name.iteritems():
            for raw, col in columns.iteritems():
                command += """ %s."%s" varchar, """ % (cf, col)
        command = command[:-2] + """)"""
        logger.debug(command)
        cursor.execute(command)
        cursor.close()
    except Exception as e:
        logger.error("create view error, the error info is %s " % e)
        raise e


def create_table(cursor, table_name, columns_name):
    try:
        command = """create table if not exists "%s" ( rowkey varchar not null primary key, """ % table_name
        for cf, columns in columns_name.iteritems():
            for raw, col in columns.iteritems():
                command += """ %s."%s" varchar, """ % (cf, col)
        command = command[:-2] + """)"""
        logger.debug(command)
        cursor.execute(command)
        cursor.close()
    except Exception as e:
        logger.error('create table error, the error info is %s ' % e)
        raise e


def drop_view(cursor, view_name):
    try:
        cursor.execute("""drop view "%s" """ % view_name)
        cursor.close()
    except Exception as e:
        logger.error("drop view error, the error info is %s" % e)
        raise(e)


def drop_table(cursor, table_name):
    try:
        cursor.execute("drop table \"%s\"" % table_name)
        cursor.close()
    except Exception as e:
        logger.error("drop table error, the error info is %s" % e)


def create_index_condition(columns_name, index_items, include_items=None):
    command = """("""
    include = """include ("""
    for cf, columns in columns_name.iteritems():
        for raw, col in columns.iteritems():
            if raw in index_items:
                command += """ %s."%s", """ % (cf, col)
            if raw in include_items:
                include += """ %s."%s", """ % (cf, col)
    if include_items is not None:
        command = command[:-2] + """) """
        command += include[:-2] + """)"""
    return command


def create_index(cursor, index_name, table_name, index_condition):
    try:
        command = """create index "{index_name}" on "{table_name}" {index_condition}""".format(
            index_name=index_name,
            table_name=table_name,
            index_condition=index_condition,
        )
        logger.debug(command)
        cursor.execute(command)
        cursor.close()

    except Exception as e:
        logger.error('create index failed, the error info is %s ' % e)
        raise e


def alter_index(cursor, index_name, table_name):
    try:
        command = """alter index "{index_name}" on "{table_name}" rebuild""".format(
            index_name=index_name,
            table_name=table_name,
        )
        logger.debug(command)
        cursor.execute(command)
        cursor.close()
    except Exception as e:
        logger.error('alter index failed, the error info is %s ' % e)
        raise e


def drop_index(cursor, index_name, table_name):
    try:
        command = """drop index "{index_name}" on "{table_name}" """.format(
            index_name=index_name,
            table_name=table_name,
        )
        logger.debug(command)
        cursor.execute(command)
        cursor.close()
    except Exception as e:
        logger.error('drop index failed, the error info is %s ' % e)
        raise e
