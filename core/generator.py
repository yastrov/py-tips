#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Generator examples, snippets.
"""

def numerate(iterable, num=0):
    """Core enumerate function analog"""
    n = 0
    for x in iterable:
        yield (n, x)
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
def walk(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            fname = os.path.join(root, name)
            yield fname

def fibonacchi(n):
    """
    Fibonacchi numbers.
    >>> list(fibonacchi(5))
    [0, 1, 1, 2, 3, 5]
    """
    a, b = 0, 1
    yield a
    yield b
    i = 2
    n += 1
    # for _ in range(2, n):
    while i < n:
        F = b+a
        yield F
        a = b
        b = F
        i+=1

def get_pair(iterable, fil=None):
    """
    get_pair([1,2,3,4]) --> [1,2] [3,4]
    >>> list(get_pair([1, 2, 3, 4]))
    [[1, 2], [3, 4]]
    >>> list(get_pair([1, 2, 3]))
    [[1, 2], [3, None]]
    """
    pool = list(iterable)
    if len(pool)%2 != 0:
        pool.append(fil)
    i = 0
    while i < len(pool):
        yield pool[i:i+2]
        i += 2

def get_pair2(iterable, fil=None):
    """
    get_pair2([1,2,3,4]) --> [1,2] [3,4]
    >>> list(get_pair2([1, 2, 3, 4]))
    [[1, 2], [3, 4]]
    >>> list(get_pair2([1, 2, 3]))
    [[1, 2], [3, None]]
    """
    result = [None, None]
    # If comment next block, you may use it with
    # all iterators, but the last element without a pair will be skipped.
    # pool = iterable
    # start
    pool = list(iterable)
    if len(pool)%2 != 0:
        pool.append(fil)
    # end
    it = iter(pool)
    while True:
        result[0] = next(it)
        result[1] = next(it)
        yield result

def get_num_from_list(iteration, num=2, fil=None):
    """
    Get num elements from iteration (full iteration support with
    bufferisation on the end step.) and complete chain with fill,
    if needs more elements for complete.
    >>> list(get_num_from_list([1, 2, 3, 4], num=3, fill=None))
    [[1, 2, 3], [4, None, None]]
    """
    i = iter(iteration)
    while True:
        result = []
        # yield [next(i) for _ in range(num)]
        for _ in range(num):
            try:
                result.append(next(i))
            except StopIteration:
                while len(result) < num:
                    result.append(fill)
                yield result
                raise StopIteration
        yield result

if __name__ == '__main__':
    for n, el in numerate(['a','b','c']):
        print("{} - {}".format(n, el))

    s = os.getcwd() #Get current dir
    for path in walk(s):
        print(path)
