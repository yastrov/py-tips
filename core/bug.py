#!/usr/bin/env python3
#encoding: utf-8

def f():
    try:
        raise KeyError #Or other Exception
    finally:
        return 5

f()
#It returns 5
