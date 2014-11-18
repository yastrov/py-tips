#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Iterator examples, snippets.
Also this snippet may be one solid class,
which contain __next__ and __iter__.
"""

class Iterator:

    def __init__(self, max_int):
        self.it = 0
        self.max_int = max_int

    # Only __next__(self):
    def __next__(self):
        self.it = self.it + 1
        if self.it > self.max_int:
            raise StopIteration
        return self.it


class WrapperIterator:

    def __init__(self, max_int):
        self.max_int = max_int

    def __iter__(self):
        return Iterator(self.max_int)


# Second var: only one class
class IterB:
    def __init__(self, max_int):
        self.max_int = max_int
        self.it = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.it = self.it + 1
        if self.it > self.max_int:
            raise StopIteration
        return self.it

if __name__ == '__main__':
    for x in WrapperIterator(5):
        print(x)

    #next() default example
    it = IterB(2)
    while True:
        n = next(it, None)
        print(n)
        if n is None:
            break

    #Callable iter example:
    #Call input, while user do not enter '5'
    [int(x) for x in iter(input, '5')]

    from functools import partial
    with open() as f
        chunks = [chunk for chunk in iter(partial(f.read, 32), '')]
