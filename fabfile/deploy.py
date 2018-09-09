#!/usr/bin/env python

import os

from fabric.api import (
    cd,
    env,
    run,
    task,
    roles,
    local,
    prefix,
)

env.roledefs = {
  'prod': ['root@47.93.0.160']
}

@task
@roles('prod')
def prod(reset=False):
  with cd('/work/new7day/'):
    if reset:
        run('git reset --hard HEAD~1')
    else:
        run('git checkout -- .')
    run('git pull --rebase origin master')
    migrate()

@task
@roles('prod')
def migrate():
  with cd('/work/new7day/'):
    with prefix('workon new7day'):
      run('python manage.py makemigrations')
      run('python manage.py migrate')
      run('uwsgi --reload scripts/uwsgi.pid')
    




