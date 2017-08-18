#!/usr/bin/env python
# -*- coding: utf-8 -*-
__doc__ = """
Обойдём и что-нибудь сделаем с каждым файлом в папке.
Универсальный вариант.
Функциональный стиль (используются только функции)

walk_over_path полностью универсальна.
Этот скрипт может быть импортирован и использован в любой сложной
программе без редактирования.
Нужно только вызвать walk_over_path с нужными аргументами

Понятно, что могут быть некоторые вариации, но в целом логика такая.
"""

import os
# Доки на модуль https://docs.python.org/3/library/os.html

def getSize(filename):
    '''Один из способов узнать размер файла.
    Другой - вызов функции os.path.getsize.'''
    assert isinstance(fileName, str), 'fileName must be an str!'
    st = os.stat(filename)
    return st.st_size

def size_ch(filename_iterables):
    for fname in filename_iterables:
        yield fname, os.path.getsize(fname)

def walk_over_path(path):
    """
    :param path: папка (директория)
    :param user_func: пользовательская функция, которую мы должны вызвать для каждого файла
    :param userData: некие пользовательские данные (можно и ужалить отовсюду)
            здесь мы просто передаём их дальше, и что они такое - нам не важно
    :return: 
    """
    for root, dirs, files in os.walk(path):
        # на каждом шаге вызова os.walk мы получим
        # директорию root, список папок в ней dirs и файлов files
        # забегая сильно вперёд: os.walk возвращает "генератор" (см. yield),
        # поддерживающий обход себя с помощью итераторов
        # по которому мы можем проходить for-ом
        print('We now at folder: {}'.format(root))
        print('Dirs: {}'.format(dirs))
        print('Files: {}'.format(files))
        for file in files:
            yield os.path.join(root, file)


def main():
    """
    Главный код скрипта принято оформлять в функции main, видимо с языка Си
    :return: 
    """
    path = "C:\\Users"
    size_all = 0
    for file_path, file_size in size_ch(walk_over_path(path)):
        size_all = size_all + file_size
        # os.remove(file_path)
        # os.rename(file_path, file_path+'.bacup')
    # Зря мы что-ли с пользовательскими данныи заморачивались?
    print('All size in bytes: {}'.format(size_all))
    return 0


# Проверка, что скрипт запущем самостоятельным и независимым
if __name__ == '__main__':
    main()
