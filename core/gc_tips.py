#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import weakref
"""
Some Garbage Collector tips

http://asvetlov.blogspot.ru/2013_05_01_archive.html
https://tech.yandex.ru/events/yagosti/19-july-2014/talks/2075/

Do not override (rewrite) __del__ method! GC don't collect it (GC is not very smart).
__del__ is not C++ destructor.
[del x] is not mean x.__del__()

import gc
# If we must control execution of program: Disable
gc.disable()

# See for memory
gc.get_count()[0]

# Catch cycles
gc.set_debug(gs.DEBUG_SAVEALL)
gc.collect()
gc.garbage

# If GC enabled, you can control population
gc.get_threshold()
gc.set_threshold(10000, 10, 10)
"""
################################
# See for cycles in memory after GC work
# gc.garbage and objgraph
# sudo pip3 install objgraph
# sudo apt-get install xdot
class B():
    def __init__(self, a):
        self.a = a
        #Solution
        #self.a = weakref.ref(a)


class A():
    def __init__(self):
        self.b = B(self)

def main():
    a = A()
    a = None

if __name__ == '__main__':
    import gc, objgraph, inspect
    main()
    gc.set_debug(gc.DEBUG_SAVEALL)
    gc.collect()
    isclass = inspect.isclass #My optimization
    ignore = lambda x: not isclass(x)
    objgraph.show_refs(gc.garbage,
        filename='graph.png', max_depth=4,
        filter=ignore)

##############################
# weakref
# Example for Py 2.7
# Use for free from cycles
import weakref
class A(object):
    def __init__(self):
        self.callback = None

    def bind(self, callback):
        self.callback = callback

def main():
    a = A()
    weak_a = weakref.ref(a)
    def some_callback(obj2):
        # Bad idea: a == obj
        # Cycles and problem in GC
        # Right solution:
        if weak_a() == obj:
            print('main object')
        else:
            print('non main object')
    a.bind(some_callback)