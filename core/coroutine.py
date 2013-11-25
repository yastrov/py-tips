#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Coroutines.
http://dabeaz.com/coroutines/

Profit: It may be faster.

Copyright (C) 2009, All Rights Reserved
David Beazley

David Beazley use it for Event processing, 
XML parsing, State Machine.
(For more examples, see presentation from link)

Also, if you work with many threads and processes, except:
StopIteration
OSError
and close pipe.

See PEP 342
"""

# A decorator function that takes care of starting a coroutine
# automatically on call.
import time
from functools import wraps

def coroutine(func):
    @wraps(func)
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

def follow(thefile, target):
    thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         target.send(line)

# A filter.

@coroutine
def grep(pattern,target):
    while True:
        line = (yield)           # Receive a line by send(msg)
        if pattern in line:
            target.send(line)    # Send to next stage

# A sink.  A coroutine that receives data

# g = grep("python", target)
# g.next()
# g.send("python_3.3")

@coroutine
def printer():
    while True:
         line = (yield)
         print line,

# Example use
if __name__ == '__main__':
    f = open("access-log")
    follow(f,
           grep('python',
           printer()))