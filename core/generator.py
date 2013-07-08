#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Generator examples, snippets.
"""

def numerate(lst, num=0):
    """Core enumerate function analog"""
    n = 0
    for l in lst:
        yield (n, l)
        n += 1

def filereader(fname, encoding='utf-8'):
    """Simple file reader on generator"""
    with open(fname, 'r', encoding=encoding) as f:
        for line in f:
            l = line.strip()
            if l.startswith('#'):
                continue
            elif l == '':
                continue
            yield l

import os
def walk(self, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            fname = os.path.join(root, name)
            yield fname

if __name__ == '__main__':
    for n, el in numerate(['a','b','c']):
        print("{} - {}".format(n, el))

    s = os.getcwd() #Get current dir
    for path in walk(s):
        print(path)