#!/usr/bin/env python

import os

from fabric.api import (
    task,
    local,
)
from datetime import datetime

from new7day import settings

DATABASES = settings.DATABASES['default']

@task
def manage(cmd):
    local(
        'python manage.py {cmd}'.format(cmd=cmd)
    )

@task
def migrate():
    '''
    数据库迁移
    '''
    manage('makemigrations')
    manage('migrate')

@task
def create_db():
    '''
    创建数据库
    '''
    kwargs = dict(
        db_name=DATABASES['NAME'],
        db_password=DATABASES['PASSWORD'],
    )
    local(
        'mysql -uroot -p{db_password} -e '
        '"CREATE DATABASE IF NOT EXISTS {db_name};"'.format(**kwargs)
    )


@task
def drop_db():
    '''
    删除数据库
    '''
    kwargs = dict(
        db_name=DATABASES['NAME'],
        db_password=DATABASES['PASSWORD'],
    )
    local(
        'mysql -uroot -p{db_password} -e '
        '"DROP DATABASE {db_name};"'.format(**kwargs)
    )

@task
def backup():
    '''
    数据备份
    '''
    if not os.path.exists('./backup'):
        local('mkdir backup')
    now = datetime.now().strftime('%Y%m%d%H%M')
    kwargs = dict(
        now=now,
        db_name=DATABASES['NAME'],
        db_password=DATABASES['PASSWORD'],
    )
    local(
        'mysqldump -uroot -p{db_password} '
        '{db_name} > ./backup/common_data_{now}.sql;'
        'cp ./backup/common_data_{now}.sql ./backup/data.sql'.format(**kwargs)
    )


@task
def recovery(sql_file=None):
    '''
    数据导入
    '''
    filename = './backup/data.sql' if not sql_file else sql_file
    drop_db()
    create_db()
    kwargs = dict(
        filename=filename,
        db_name=DATABASES['NAME'],
        db_password=DATABASES['PASSWORD'],
    )
    local(
        'mysql -uroot -p{db_password} '
        '{db_name} < {filename}'.format(**kwargs)
    )

