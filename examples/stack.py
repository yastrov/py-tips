#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque

class LIFO_Stack(object):
    """LIFO stack"""

    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def pop_or_none(self):
        if self.is_empty():
            return None
        return self.pop()

    def peek(self):
        return self._items[-1]

    def peek_or_none(self):
        if self.is_empty():
            return None
        return self.peek()

    def size(self):
        return len(self._items)

    def __str__(self):
        return '.'.join(self._items)


class FIFO_StackD(object):
    """FIFO stack"""

    def __init__(self):
        self._items = deque()

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def extend(self, iterable):
        self._items.extend(item)

    def pop(self):
        return self._items.popleft()

    def pop_or_none(self):
        if self.is_empty():
            return None
        return self.pop()

    def peek(self):
        return self._items[-1]

    def peek_or_none(self):
        if self.is_empty():
            return None
        return self.peek()

    def size(self):
        return len(self._items)

    def __str__(self):
        return '.'.join(self._items)


class LIFO_StackD(object):
    """LIFO stack"""

    def __init__(self):
        self._items = deque()

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.appendleft(item)

    def extend(self, iterable):
        self._items.extendleft(item)

    def pop(self):
        return self._items.popleft()

    def pop_or_none(self):
        if self.is_empty():
            return None
        return self.pop()

    def peek(self):
        return self._items[-1]

    def peek_or_none(self):
        if self.is_empty():
            return None
        return self.peek()

    def size(self):
        return len(self._items)

    def __str__(self):
        return '.'.join(self._items)
