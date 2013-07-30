#!/usr/bin/env python3
#coding: utf-8
import logging

# Use in function
def foo():
    logger = logging.getLogger(__name__)
    logger.info('Execute foo function')

# Use in class
class FooClass:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
 
    def foo(self):
        self.logger.info('foo function in FooClass object')