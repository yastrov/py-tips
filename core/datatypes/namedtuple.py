#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For Python 3.6
from typing import NamedTuple

class Cat(NamedTuple):
    name: str
    age: int
    weight: float

my_cat = Cat('Cat name', 3, 5.4)

#######
# For all (and old) Python
from collections import namedtuple
Cat = namedtuple('Cat' , ['name', 'age', 'weight'])
# Or via tuple
Cat2 = namedtuple('Cat' , ('name', 'age', 'weight'))
my_cat = Cat('Cat name', 3, 5.4)
