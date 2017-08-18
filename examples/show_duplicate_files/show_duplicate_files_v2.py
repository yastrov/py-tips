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

# Размер файла
getSize = os.path.getsize

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

def walk(path):
    for root, dirs, files in os.walk(path):
        for _file in files:
            fname = os.path.join(root, _file)

def moreThanOne(dct):
    return {k:v for k, v in dct.items() if len(v) > 1}

def size_ch(fname_iterable):
    for fname in fname_iterable:
        yield fname, getSize(fname)

def getDuplicatesFiles(path, hash_func=sha3_512):
    assert isinstance(path, str), 'path must be an str!'
    HashFilesBySize = defaultdict(list)
    HashFilesByHash = defaultdict(list)

     # Сохраним размеры для каждого файла в папке в хэш таблицу
    for fname, fsize in size_ch(walk(path)):
        HashFilesBySize[fsize].append(fname)

    # Удалим информацию о файлах, с уникальными размерами
    HashFilesBySize = moreThanOne(HashFilesBySize)

    # Посчитаем хэши
    for key, values in HashFilesBySize.items():
        for fname in values:
            hash_key = hash_func(fname)
            if hash_key is None:
                continue
            HashFilesByHash[hash_key].append(fname)
    HashFilesBySize.clear()

    # Удалим информацию о файлах, с уникальными хэшами
    HashFilesByHash = moreThanOne(HashFilesByHash)
    return HashFilesByHash


def main():
    global path
    HashFilesByHash = getDuplicatesFiles(path)
    # Выведем список файлов пользователю
    for key, values in HashFilesByHash.items():
        print('----------')
        print('Hash {}'.format(key))
        for value in values:
            print('\t{}'.format(value))

# Проверка, что скрипт запущем самостоятельным и независимым
if __name__ == '__main__':
    main()
