import logging.config

from conf import config
from conf.constants import (
    COMMAND_STATE,
)


logging.config.fileConfig(config.LOG_CONFIG_LOCATION)
logger = logging.getLogger(__name__)


def push_command_to_redis(vin, command_package, redis_conn):
    """
    Push command package in binary format to redis

    :type vin: str
    :type command_package: str
    :type redis_conn: redis.StrictRedis
    """
    logger.debug('Push command to vin {vin}, package content: {command}'.format(
        vin=vin,
        command=command_package.encode('hex'),
    ))
    key = 'commands:' + vin

    redis_conn.hset(key, command_package, COMMAND_STATE.UNTREATED)
