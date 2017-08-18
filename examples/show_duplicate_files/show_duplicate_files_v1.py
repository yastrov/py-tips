#!/usr/bin/env python
# -*- coding: utf-8 -*-
__doc__ = '''This is simple duplicate files finde script.

Это простой скрипт для поиска копий (дубликатов) файлов.
'''

from collections import defaultdict
import os
import hashlib

# Путь, директория, которую будем обрабатывать
path = "C:\\Users"

def getSize(filename):
    '''Один из способов узнать размер файла.
    Другой - вызов функции os.path.getsize.'''
    st = os.stat(filename)
    return st.st_size

def sha3_512(fname, blocksize=4096):
    '''Вычисление хэш суммы файла, считывая порциями по blocksize байт'''
    hash_sha3_512 = hashlib.sha3_512()
    try:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(blocksize), b""):
                hash_sha3_512.update(chunk)
        return hash_sha3_512.hexdigest()
    except IOError as e:
        print(e)
        return None

HashFilesBySize = defaultdict(list)
HashFilesByHash = defaultdict(list)

# Сохраним размеры для каждого файла в папке в хэш таблицу
for root, dirs, files in os.walk(path):
    for _file in files:
        fname = os.path.join(root, _file)
        fsize = os.path.getsize(fname)
        HashFilesBySize[fsize].append(fname)

# Удалим информацию о файлах, с уникальными размерами
HashFilesBySize = {k:v for k, v in HashFilesBySize.items() if len(v) > 1}

# Посчитаем хэши
for key, values in HashFilesBySize.items():
    for fname in values:
        hash_key = sha3_512(fname)
        if hash_key is None:
            continue
        HashFilesByHash[hash_key].append(fname)
HashFilesBySize.clear()

# Удалим информацию о файлах, с уникальными хэшами
HashFilesByHash = {k:v for k, v in HashFilesByHash.items() if len(v) > 1}

# Выведем список файлов пользователю
for key, values in HashFilesByHash.items():
    print('----------')
    print('Hash {}'.format(key))
    for value in values:
        print('\t{}'.format(value))
