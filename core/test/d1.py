#!/usr/bin/env python
#encoding: utf-8

__doc__ = """Doctest examples, snippets.
Test in __doc__.

Use:
python3 -m doctest d1.py -v
"""

def summ(a, b):
    """Sum two arguments
    >>> summ(1, 2)
    3"""
    return a+b

if __name__ == '__main__':
    pass
