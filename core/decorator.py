#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Wrappers (Decorators) examples, snippets.

@functools.wraps копирует специальные атрибуты
из оборачиваемой функции и мы получаем красивое 
понятное сообщение об ошибке.
"""

from functools import wraps

def dec(f):
    @wraps(f)
    def wrapper (*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

def decor(value):
    def decorator(f):
        print(value)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper
    return decorator

import time
def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        t2 = time.time()
        print("{} - time: {}".format(f, t2 - t1))
        return res
    return wrapper

@decor('It decor.')
@timer
def foo(name):
    """Doc string"""
    print('Hello {}!'.format(name))

if __name__ == '__main__':
    foo('user')
    print(foo.__doc__)#Provides by @wraps