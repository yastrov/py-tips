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


def process_file(fileName, userData=None):
    """
    Функция, которая принимает полный путь к файлу и сто-то с ним делает
    :param fileName: 
    :param userData: некие пользовательские данные (можно и ужалить отовсюду)
    :return: 
    """
    # Проверка безопасности (вдруг нас вызовут с числом или какой-нибудь пакостью?)
    assert isinstance(fileName, str), 'fileName must be an str!'
    info = os.stat(fileName)
    print('File: {} with size: {} bytes'.format(fileName, info.st_size))
    userData.append(info.st_size)
    # os.remove(current_path)
    # os.rename(current_path, current_path+'.bacup')


def walk_over_path(path, user_func, userData=None):
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
            user_func(current_path, userData)


def main():
    """
    Главный код скрипта принято оформлять в функции main, видимо с языка Си
    :return: 
    """
    path = "C:\\Users"
    MyData = []
    # Указываем нашу функцию process_file
    walk_over_path(path, process_file, MyData)
    # Зря мы что-ли с пользовательскими данныи заморачивались?
    size_all = 0
    for fsize in MyData:
        size_all = size_all + fsize
    print('All size in bytes: {}'.format(size_all))
    # или воспользуемся стандартным приёмом Python:
    size_all = sum(MyData)
    print('All size in bytes: {}'.format(size_all))
    return 0


# Проверка, что скрипт запущем самостоятельным и независимым
if __name__ == '__main__':
    main()
