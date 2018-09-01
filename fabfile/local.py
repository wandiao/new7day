#!/usr/bin/env python

import os

from fabric.api import (
    task,
    local,
)

@task
def manage(cmd):
    local(
        'python manage.py {cmd}'.format(cmd=cmd)
    )

@task
def migrate():
    manage('makemigrations')
    manage('migrate')

