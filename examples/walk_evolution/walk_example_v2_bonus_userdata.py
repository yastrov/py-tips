#!/usr/bin/env python
# -*- coding: utf-8 -*-
__doc__ = """
Обойдём и что-нибудь сделаем с каждым файлом в папке.
Более удобный и разумный вариант
"""

import os
# Доки на модуль https://docs.python.org/3/library/os.html

# Путь, директория, которую будем обрабатывать
path = "C:\\Users"
# Глобальная переменная, сюда будем накапливать размер файлов в байтах
size_all = 0

# Предпложим, мы хотим передавать какую-нибудь информацию, но не хотим хранить её
# глобально в скрипте (более гибкое поведение)

def process_file(fileName, userData):
    """
    Функция, которая принимает полный путь к файлу и что-то с ним делает
    :param fileName: 
    :param userData: 
    :return: 
    """
    #Проверка безопасности (вдруг нас вызовут с числом или какой-нибудь пакостью?)
    assert isinstance(fileName, str), 'fileName must be an str!'
    fsize = os.path.getsize(current_path)
    print('File: {} with size: {} bytes'.format(fileName, fsize))
    userData.append(fsize)
    # os.remove(current_path)
    # os.rename(current_path, current_path+'.bacup')

# Будет выполнена при любом запуске или импорте этого скрипта
path = "C:\\Users"
MyData = []
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
        process_file(current_path, MyData)

# Зря мы что-ли с пользовательскими данныи заморачивались?
size_all2 = 0
for fsize in MyData:
    size_all2 = size_all2 + fsize
print('All size in bytes: {}'.format(size_all2))
# или воспользуемся стандартным приёмом Питона:
size_all2 = sum(MyData)
print('All size in bytes: {}'.format(size_all2))
