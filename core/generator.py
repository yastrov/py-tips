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

    Author Yuri Astrov
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

    Author Yuri Astrov
    """
    assert isinstance(iterable, (list, tuple)), 'Invalid input "iterable" argument type in get_pair(), should be list or tuple, received %s' % type(iterable)
    def unl(itera):
        yield from itera
        while True: yield fil
    for first_el, second_el in zip(iterable[::2], unl(iterable[1::2])):
        yield first_el, second_el

def get_pair3(iterable, fil=None):
    """Best approach!
    get_pair3([1,2,3,4]) --> (1,2) (3,4)
    >>> list(get_pair3([1, 2, 3, 4]))
    [(1, 2), (3, 4)]
    >>> list(get_pair3([1, 2, 3]))
    [(1, 2), (3, None)]
    >>> list(get_pair3((x for x in range(6))))
    [(0, 1), (2, 3), (4, 5)]
    >>> list(get_pair3((x for x in range(7))))
    [(0, 1), (2, 3), (4, 5), (6, None)]

    Author Yuri Astrov
    """
    it = iter(iterable)
    result = [None, fil]
    flag = True
    while flag:
        result[0] = next(it)
        try:
            result[1] = next(it)
        except StopIteration as e:
            result[1] = fil
            flag = False
        yield tuple(result)
        #If you want to return list, you should put result = [..]
        # to inside while loop.

def get_num_from_list(iteration, num=2, fil=None):
    """
    Get num elements from iteration (full iteration support with
    bufferisation on the end step.) and complete chain with fill,
    if needs more elements for complete.
    >>> list(get_num_from_list([1, 2, 3, 4], num=3, fil=None))
    [(1, 2, 3), (4, None, None)]

    >>> list(get_num_from_list((x for x in range(6)), num=3, fil=None))
    [(0, 1, 2), (3, 4, 5)]
    >>> list(get_num_from_list((x for x in range(7)), num=3, fil=None))
    [(0, 1, 2), (3, 4, 5), (6, None, None)]

    Author Yuri Astrov
    """
    i = iter(iteration)
    result = []
    flag = True
    while flag:
        # yield [next(i) for _ in range(num)]
        for _ in range(num):
            try:
                result.append(next(i))
            except StopIteration:
                if not result: return
                while len(result) < num:
                    result.append(fil)
                flag = False
        yield tuple(result)
        result.clear()

def get_num_from_list2(iterable, num=2, fil=None):
    """
    Get num elements from iteration (full iteration support with
    bufferisation on the end step.) and complete chain with fill,
    if needs more elements for complete.
    >>> list(get_num_from_list2([1, 2, 3, 4], num=3, fil=None))
    [[1, 2, 3], [4, None, None]]

    Author Yuri Astrov
    """
    assert isinstance(iterable, (list, tuple)), 'Invalid input "iterable" argument type in get_num_from_list2(), should be list or tuple, received %s' % type(iterable)
    def unl(itera):
        yield from itera
        while True: yield fil
    para = [iterable[i::num] if i%num == 0 else unl(iterable[i::num])
                for i in range(num)]
    return zip(*para)

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