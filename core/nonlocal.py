#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://www.slideshare.net/MinskPythonMeetup/ss-28237758
# http://www.youtube.com/watch?feature=player_embedded&v=gOW_V7DKm1E

# For UnboundLocalError

#Py 2.x
#def Counter(x):
#    a = [x]
#    def zero():
#        a[0] = 0
#    def val():
#        return a[0]
#    def inc():
#        a[0] += 1
#        return a[0]
#    return (zero, val, inc)

def Counter(x):
    a = x
    def zero():
        nonlocal a
    def val():
        return a
    def inc():
        nonlocal a
        a += 1
        return a
    return (zero, val, inc)

zero, val, inc = Counter(5)
print(zero())
print(val())
print(inc())
