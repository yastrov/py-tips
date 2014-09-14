#!/usr/bin/env python
# -*- coding: utf-8 -*-
__doc__ = """
Calculate eval time of script or function.

Also see
http://pythonfasterway.uni.me/
https://github.com/zokis/Python--Faster-Way

python3 -m cProfile time_test.py"""
def foo(): return [x for x in range(5)]

from timeit import timeit
timeit(foo, number=1000000)

import timeit
timeit.repeat("foo()", "from __main__ import foo",
      number=1000000)
