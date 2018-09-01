#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging.config

from conf import config

logging.config.fileConfig(config.LOG_CONFIG_LOCATION)
logger = logging.getLogger(__name__)


def get_common_logger(name='common', logfile=None):
    """
    参数: name (str): logger name
        logfile (str): log file, 没有时使用stream handler
    返回:
        logger obj
    """
    my_logger = logging.getLogger(name)
    my_logger.setLevel(config.LOG_LEVEL)
    if logfile:
        handler = logging.FileHandler(logfile)
    else:
        handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(formatter)
    my_logger.addHandler(handler)
    # 阻止冒泡
    my_logger.propagate = False
    return my_logger


def get_obd_logger():
    return logger


LOGGER = get_common_logger()
