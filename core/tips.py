#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Basic tips and trics.

For profiling:
python3 -m cProfile [-o output_file] [-s sort_order] myscript.py

Dissasembling:
from dis import dis

def foo(): return 1
dis(foo)

gen = (x for x in range(100))
dis(gen.gi_code)
"""

# For perfomance: Optimizing time for access
import os
pjoin = os.path.join

# Advanced unpack
a, b, *args, c  = range(10)

# Unix epoha time in secunds
epoch_time = int(time.time())

a = 3
b = 7
#Swap
a, b = b, a

# Lexical scoping
# It working with independed cell object
# lambda and closure exqmple
# lambda при "получении" переменной запоминает ее название и scope.
# Scope глобальный и когда происходит реальный вызов функции,
# используется последнее значение i. Чтобы избежать этого:
lambdas = [lambda a, i=i: a + i for i in range(5)]
l = [l(1) for l in lambdas]

l = [lambda x=x: x for x in "abcdefg"]
for r in l: print(r())

# from codecs import open #For Python 2.7
with open(filename, 'wb', encoding='utf-8') as f:
    f.write(3)

with open(filename1, 'r') as fi, open(filename2, 'w') as fo:
    pass

# Read chunks with size 32, while data from file is not '' 
from functools import partial
with open() as f
    chunks = [chunk for chunk in iter(partial(f.read, 32), '')]

from io import StringIO, BytesIO
#StringIO Реализует интерфейс работы с файлами для строк
#BytesIO Реализует интерфейс работы с файлами для строк
#В Python работа идет в соответствии с интерфейсом, а не типом объекта.

# for access to vars:
vars() # Also vars(obj) if obj has __dict__
locals()
globals()

def foo(arg=None, key=None):
    x = arg or []
    key = key or lambda x: x

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, [2,3,4], age=23) # age in kwargs, others in args
func({"age":23}) # dict in args
func(**{"age":23}) # dict in kwargs, '**' - unpack dict
func(*[1,2,3]) # Unpack list to *args

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
    return 1, 2

# variables:
# http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html
# Use 'global <varname>' or 'nonlocal <varname>'
# Local objects and consts saved in code object.
# Cache var or function to local is good idea for perfomance.
# global var
x = 9
def outer():
    # enclosed level for 'inner' function.
    x = 3
    print('before:', x)
    def inner():
        # local level
        nonlocal x # take enclosed x
        x = 5
        print("inner:", x)
    inner()
    print("after:", x)

# Optimisation loop hoisting (Just example!)
# Optimize LOAD_ATTR and access to __dict__
def f():
    l = []
    la = l.append
    for i in range(10000): la(i)
    return l
# list comprehensions more faster and has own opcode LIST_APPEND

import sys
if sys.stdout.isatty():
    # You're running in a real terminal
    # Use output format for user
else:
    # You're being piped or redirected
    # Use output format for simple parsing with other utilitys

# Best way (for Django or Flask or virtualenv) to add path to sys.path for
#default Python importer.
sys.path.insert(0, os.getcwd())

if __name__ == '__main__':
    # You're started as main module
else:
    # You're loaded from other module
