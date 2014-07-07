#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Basic tips and trics.

For profiling:
python3 -m cProfile [-o output_file] [-s sort_order] myscript.py
"""

# For perfomance: Optimizing time for access
import os
pjoin = os.path.join

# Advanced unpack
a, b, *args, c  = list(range(10))

# Unix epoha time in secunds
epoch_time = int(time.time())

a = 3
b = 7
#Swap
a, b = b, a

# lambda and closure exqmple
lambdas = [lambda a, i=i: a + i for i in range(5)]
l = [l(1) for l in lambdas]

# from codecs import open #For Python 2.7
with open(filename, 'wb', encoding='utf-8') as f:
    f.write(3)

with open(filename1, 'r') as fi, open(filename2, 'w') as fo:
    pass

from io import StringIO, BytesIO
#StringIO Реализует интерфейс работы с файлами для строк
#BytesIO Реализует интерфейс работы с файлами для строк
#В Python работа идет в соответствии с интерфейсом, а не типом объекта.

def foo(arg=None):
    x = arg or []

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, [2,3,4], age=23) # age in kwargs, others in args
func({"age":23}) # dict in args
func(**{"age":23}) # dict in kwargs

#Keyword only argumant
def f(a, b, *args, option=True):
    print(args)

def best_return():
    """
    Optimizing return from function. Not create var before return.
    dis from dis module are confirms.
    Оптимальный код возврата из функции - без предварительного создания переменной.
    """
    # Not a = (1,2)
    return (1, 2)

import sys
if sys.stdout.isatty():
    # You're running in a real terminal
    # Use output format for user
else:
    # You're being piped or redirected
    # Use output format for simple parsing with other utilitys

if __name__ == '__main__':
    # You're started as main module
else:
    # You're loaded from other module
