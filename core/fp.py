#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """
Functional programming examples.

Based on:
http://kachayev.github.io/talks/uapycon2012/index.html#/
"""

from operator import add, mul
import math
from functools import reduce

expr = "28+32+++32++39"
reduce(add, map(int, filter(bool, expr.split("+"))))
r2 = sum(map(int, filter(bool, expr.split("+"))))

st = ["UA", "PyCon", "2012"]
r1 = reduce(add, map(len, st))
r2 = sum(map(len, st))

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

# Hints
map(str, range(5))

class Speaker(object):
    def __init__(self, name):
        self.name = name
map(Speaker, ["Alexey", "Andrey", "Vsevolod"])