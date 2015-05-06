#encoding: utf-8
"""
Read binary file in special format and save to namedtuple.
"""
import struct
from collections import namedtuple

fname = ""

Item = namedtuple('Item', ['number', 'type',
                           'sizep', 'path',
                           'sizef', 'filename'])
items = []
with open(fname, 'rb') as f:
    # считываем количество записей
    buffer = f.read(4)
    count = struct.unpack("i", buffer)[0]
    print("Количество записей: ", count)
    i = 0
    while i < count:
        i += 1
        print("--------")
        # считываем номер и тип файла: 2 int = 8 byte
        buffer = f.read(8)
        number, typeF = struct.unpack("ii", buffer)
        print("Номер записи: ", number)
        print("Тип: ", typeF)
        # Path
        buffer = f.read(4)
        sizeP = struct.unpack("i", buffer)[0]
        buffer = f.read(sizeP)
        FilePath = buffer.decode('utf-8')
        print(FilePath)
        # File Name
        buffer = f.read(4)
        sizeF = struct.unpack("i", buffer)[0]
        buffer = f.read(sizeF)
        FileName = buffer.decode('utf-8')
        print(FileName)
        item = Item(number, typeF,
                    sizeP, FilePath,
                    sizeF, FileName)
        items.append(item)

# Распечатаем адреса файлов
for item in items:
    print(item.path)
