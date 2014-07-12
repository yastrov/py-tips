#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Generator examples, snippets.
"""

# generator expression = выражение - генератор
# создаётся с помощью круглых скобок. В квадратных будет обычный список!
f = (x*2 for x in range(5))

def double_range(stop):
    """
    This is very simple example for "yield from".
    In old style:
    for x in range(stop):
        yield x
    """
    yield from range(stop)
    yield from range(stop)

def numerate(iterable, num=0):
    """Core enumerate function analog"""
    n = 0
    for x in iterable:
        yield n, x
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
    pjoin = os.path.join
    for root, dirs, files in os.walk(path):
        for name in files:
            yield pjoin(root, name)

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
    while i < n:
        F = b + a
        yield F
        a, b = b, F
        i+=1
        
def fibonacchi2(n):
    """
    Fibonacchi numbers.
    >>> list(fibonacchi(5))
    [0, 1, 1, 2, 3, 5]
    """
    a, b = 0, 1
    for _ in range(n+1):
        yield a
        a, b = b, b + a

def get_pair(iterable, fil=None):
    """Best approach!
    get_pair([1,2,3,4]) --> [1,2] [3,4]
    >>> list(get_pair([1, 2, 3, 4]))
    [(1, 2), (3, 4)]
    >>> list(get_pair([1, 2, 3]))
    [(1, 2), (3, None)]
    """
    def unl(itera):
        yield from itera
        while True: yield fil
    for k, v in zip(iterable[::2], unl(iterable[1::2])):
        yield k, v

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
    >>> list(get_num_from_list([1, 2, 3, 4], num=3, fil=None))
    [(1, 2, 3), (4, None, None)]
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

def get_num_from_list2(iteration, num=2, fil=None):
    """
    Get num elements from iteration (full iteration support with
    bufferisation on the end step.) and complete chain with fill,
    if needs more elements for complete.
    >>> list(get_num_from_list([1, 2, 3, 4], num=3, fil=None))
    [(1, 2, 3), (4, None, None)]
    """
    def unl(itera):
        yield from itera
        while True: yield fil
    para = [iteration[i::num] if i%num == 0 else unl(iteration[i::num])
                for i in range(num)]
    for k in zip(*para):
        yield k

def f(value):
    """
    Thank for https://alexbers.com/python_quiz/
    """
    while True:
        value = (yield value)

a=f(10)
print(next(a))
print(next(a))
print(a.send(20))

if __name__ == '__main__':
    for n, el in numerate(['a','b','c']):
        print("{} - {}".format(n, el))

    s = os.getcwd() #Get current dir
    for path in walk(s):
        print(path)
    for i in get_pair([x for x in range(5)]):
        print(i)
    for i in get_num_from_list2([x for x in range(5)], num=3, fil=None):
        print(i)