#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
New yield from
"""

# chain from itertools with the new keyword
def chain2(*iters):
    for it in iters:
        yield from it

def foo():
    x = yield from range(7)
    if x is not None:
        yield x
    else:
        print('The end of foo.')

def fromrange(x):
    yield from range(x)

if __name__ == '__main__':
    for y in chain2([0,2,3,4,5,6]):
        print(y)
    print('-')
    for y in foo():
        print(y)
    print('-')
    for y in fromrange(7):
        print(y)