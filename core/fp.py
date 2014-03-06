#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """
Functional programming examples.

Based on:
http://kachayev.github.io/talks/uapycon2012/index.html#/
"""

print((lambda x: x**2)(6))

from operator import add, mul
import math
from functools import reduce
from itertools import starmap

expr = "28+32+++32++39"
reduce(add, map(int, filter(bool, expr.split("+"))))
r2 = sum(map(int, filter(bool, expr.split("+"))))

st = ["UA", "PyCon", "2012"]
r1 = reduce(add, map(len, st))
r2 = sum(map(len, st))
#Map, for only call function.
starmap(lambda x: print(x), st)

# Recursion
def get_name():
    name = raw_input()
    return name if len(name) >= 2 else get_name()

# Currying
def square_sum(a, b):
    return sum(map(lambda x: x**2, range(a,b+1)))

def fsum(f):
    def apply(a, b):
        return sum(map(f, range(a,b+1)))
    return apply

log_sum = fsum(math.log)
square_sum = fsum(lambda x: x**2)
simple_sum = fsum(int) ## fsum(lambda x: x)
fsum(lambda x: x*2)(1, 10)
import functools
fsum(functools.partial(mul, 2))(1, 10)

basetwo = functools.partial(int, base=2)
basetwo('10010')

# Hints
map(str, range(5))

class Speaker(object):
    def __init__(self, name):
        self.name = name
map(Speaker, ["Alexey", "Andrey", "Vsevolod"])

# See, it is look like Django Objects and jQuery.
class Context:
    def __init__(self, items):
        self.__items = items

    def fmap(self, key):
        self.__items = map(key, self.__items)
        return self

    def filter(self, key):
        self.__items = filter(key, self.__items)
        return self.__items

    def result(self):
        return self.__items

l = Context([1,2,3,]).fmap(lambda x: x+1).fmap(lambda x: x*2).result()
print(list(l))

rightTriangles = [(a,b,c) for a in range(1,11) for b in range(1,11) for c in range(1,11) if a**2 + b**2==c**2 and a+b+c==24]
