#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Basic tips and trics.
"""
a = 3
b = 7
#Swap
a, b = b, a

with open(filename, 'wb', encoding='utf-8') as f:
    f.write(3)

with open(filename1, 'r') as fi, open(filename2, 'w') as fo:
    pass

from io import StringIO, BytesIO
#StringIO Реализует интерфейс работы с файлами для строк
#BytesIO Реализует интерфейс работы с файлами для строк
#В Python работа идет в соответствии с интерфейсом, а не типом объекта.
