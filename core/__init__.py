#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Use this for crossplatform package with next struct:
    package
        __init__.py (This file)
        a.py
        linux2
            b.py
        win32
            b.py

Ant then just use:
from package import b


Thank for http://asvetlov.blogspot.ru/2010/05/blog-post.html

And some about import from zip:
http://asvetlov.blogspot.ru/2010/05/3.html
"""

import sys
from os.path import join, dirname

__path__.append(join(dirname(__file__), sys.platform))

# Best way (for Django or Flask or virtualenv) to add path to sys.path for
#default Python importer.
import sys
import os
sys.path.insert(0, os.getcwd())