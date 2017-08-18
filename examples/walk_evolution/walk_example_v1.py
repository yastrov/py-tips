#!/usr/bin/env python
# -*- coding: utf-8 -*-
__doc__ = """
Обойдём и что-нибудь сделаем с каждым файлом в папке.

Самый простой и короткий, "наколенный вариант".

Примечание: чем больше версия в новом скрипте, тем универсальнее
вариант, 4 и 5 самые универсальные в своих стилях
"""

import os
# Доки на модуль https://docs.python.org/3/library/os.html

# Путь, директория, которую будем обрабатывать
path = "C:\\Users"

# Глобальная переменная, сюда будем накапливать размер файлов в байтах
size_all = 0
# Забегая вперёд:
# вызов os.walk(path) возвращает некую штуку (пока не важно какую).
# for запрашивает полученную штуку пока может
# и каждый запрос возвращает набор из 3х элементов
# Которые мы для своего удобства назвали root, dirs, files
for root, dirs, files in os.walk(path):
    # на каждом шаге мы получим
    # "текущую" директорию root, список имён папок в ней dirs и список файлов files
    print('We now at folder: {}'.format(root))
    print('Dirs: {}'.format(dirs))
    print('Files: {}'.format(files))
    for folder in dirs:
        # Соберём путь из фрагментов,
        # с учётом особенности ОС и платформы (обратных и прмяых слешей и т.п.)
        # что берёт на себя os.path.join
        current_path = os.path.join(root, folder)
        # В current_path теперь путь папки
        # Здесь мы можем сделать что-нибудь
    for file in files:
        current_path = os.path.join(root, file)
        # В current_path теперь путь к файлу
        # Здесь мы можем сделать что-нибудь
        fsize = os.path.getsize(current_path)
        print('File: {} with size: {} bytes'.format(current_path, fsize))
        size_all = size_all + fsize
        #os.remove(current_path)
        #os.rename(current_path, current_path+'.bacup')

print('All size in bytes: {}'.format(size_all))
# Но такой скрипт "одноразовый", и каждый раз нужно писать заново,
# .меняя код в разных местах
# Попробуем сделать его богглее удобным для повторного использования
