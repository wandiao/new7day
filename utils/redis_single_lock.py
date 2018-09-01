"""This module implement a lock using setnx for single node redis """
import time
import uuid
import logging


logger = logging.getLogger(__name__)


class AcquireFailed(Exception):
    pass


class Lock(object):
    """
    This is a lock used with single node redis

    :Example:
    with Lock(conn, a_lock_name):
        do something
    """

    def __init__(self, conn, lock_name, acquire_timeout=10, lock_timeout=10):
        self._conn = conn
        self._lock_name = 'lock:' + lock_name
        self._acquire_timeout = acquire_timeout
        self._lock_timeout = lock_timeout

        self._identifier = str(uuid.uuid4())

        self.locked = False

    def acquire(self):
        end_time = time.time() + self._acquire_timeout

        while time.time() < end_time:
            if self._conn.set(
                    self._lock_name,
                    self._identifier,
                    ex=self._lock_timeout,
                    nx=True):
                self.locked = True
                return True
            time.sleep(0.1)

        return False

    def release(self):
        if self._conn.get(self._lock_name) == self._identifier:
            self._conn.delete(self._lock_name)
            self.locked = False

    def __enter__(self):
        acquired = self.acquire()
        if acquired:
            return self

        logger.info(('Get lock action failed, maybe another client is '
                     'acquiring lock'))
        raise AcquireFailed('Acquire lock failed')

    def __exit__(self, exc_type, exc_value, traceback):
        logger.debug((exc_type, exc_value, traceback))
        self.release()
