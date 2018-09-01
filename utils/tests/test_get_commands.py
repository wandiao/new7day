from redis import StrictRedis

from config import config


redis_conn = StrictRedis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
)

identifier = 'c24b9998-93d9-486b-9574-ffd879b652f5'

from utils.redis_utils import get_commands

print get_commands(redis_conn, identifier)
