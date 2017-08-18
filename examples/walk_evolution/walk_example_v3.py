#!/usr/bin/env python
# -*- coding: utf-8 -*-
__doc__ = """
Обойдём и что-нибудь сделаем с каждым файлом в папке.
Более удобный и разумный вариант.
Его можно скопировать, переписать process_file под новые цели
указать новую папку и запустить.

walk_over_path трогать не нужно, оно готово.
"""

import os
# Доки на модуль https://docs.python.org/3/library/os.html


def getSize(filename):
    '''Один из способов узнать размер файла.
    Другой - вызов функции os.path.getsize.'''
    assert isinstance(fileName, str), 'fileName must be an str!'
    st = os.stat(filename)
    return st.st_size


def process_file(fileName, userData=None):
    """
    Функция, которая принимает полный путь к файлу и сто-то с ним делает
    :param fileName: 
    :param userData: некие пользовательские данные (можно и ужалить отовсюду),
            по умолчанию стоит None и при вызове можно опускать
    :return: 
    """
    #Проверка безопасности (вдруг нас вызовут с числом или какой-нибудь пакостью?)
    assert isinstance(fileName, str), 'fileName must be an str!'
    fsize = os.path.getsize(fileName)
    print('File: {} with size: {} bytes'.format(fileName, fsize))
    userData.append(fsize)
    # os.remove(fileName)
    # os.rename(fileName, fileName+'.bacup')


def walk_over_path(path, userData=None):
    """
    
    :param path: папка (директория)
    :param userData: некие пользовательские данные (можно и ужалить отовсюду)
            здесь мы просто передаём их дальше, и что они такое и есть ли они 
            - нам не важно
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
        for folder in dirs:
            # Соберём путь из фрагментов,
            # с учётом особенности ОС и платформы (обратных  прмяых слешей и т.п.)
            # что берёт на себя os.path.join
            current_path = os.path.join(root, folder)
            # В current_path теперь путь папки
            # Здесь мы можем сделать что-нибудь
        for file in files:
            current_path = os.path.join(root, file)
            # В current_path теперь путь к файлу
            # Здесь мы можем сделать что-нибудь
            process_file(current_path, userData)


def main():
    """
    Главный код скрипта принято оформлять в функции main, видимо с языка Си
    :return: 
    """
    path = "C:\\Users"
    MyData = []
    walk_over_path(path, MyData)
    # Зря мы что-ли с пользовательскими данныи заморачивались?
    size_all = 0
    for size in MyData:
        size_all = size_all + size
    print('All size in bytes: {}'.format(size_all))
    # или воспользуемся стандартным приёмом Python:
    size_all = sum(MyData)
    print('All size in bytes: {}'.format(size_all))
    return 0

# Проверка, что скрипт запущем самостоятельным и независимым
if __name__ == '__main__':
    main()
