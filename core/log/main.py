#!/usr/bin/env python3
#coding: utf-8
__doc__ = """
Logging module examples with extenal config file.
Based on examples of documentation of python and articles from WWW.
"""
import logging
import logging.config
import my

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
try:
    a = 8/0
except Exception as e:
    # Print traceback
    logger.error(e, exc_info=True)
    #or
    logger.exception(e)

# From imported module
my.foo()
