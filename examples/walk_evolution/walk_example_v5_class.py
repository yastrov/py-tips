#!/usr/bin/env python
# -*- coding: utf-8 -*-
__doc__ = """
Обойдём и что-нибудь сделаем с каждым файлом в папке.
Полностью универсальный вариант в ООП стиле (классы).

Нужно только создать наследника BaseWalker и переопределить
нужные функции.
"""

import os
# Доки на модуль https://docs.python.org/3/library/os.html


class BaseWalker:
    def __init__(self):
        """Конструктор, вызывается при создании класса
        Здесь он ничего не делает и мог быть опущен"""
        pass

    def process_file(self, fileName):
        """
        Вызывается для каждого файла.
        :param fileName: полный путь к файлу
        :return: 
        """
        # Ничего не делать
        pass

    def process_folder(self, folderName):
        """
        Вызывается для каждой папки (директории).
        :param folderName: полный путь к папке
        :return: 
        """
        # Ничего не делать
        pass

    def walk_over_path(self, path):
        """
        Главная функция класса. Всегда выхывать именно её.
        :param path: полный путь к папке, которую нужно почетить и обработать
        :return: 
        """
        for root, dirs, files in os.walk(path):
            for folder in dirs:
                # Соберём путь из фрагментов,
                # с учётом особенности ОС и платформы (обратных  прмяых слешей и т.п.)
                # что берёт на себя os.path.join
                current_path = os.path.join(root, folder)
                # Вызываем функцию нашего класса для обработки папки
                self.process_folder(current_path)
            for file in files:
                current_path = os.path.join(root, file)
                # В current_path теперь путь к файлу
                # Здесь мы можем сделать что-нибудь
                # Вызываем функцию нашего класса для обработки файла
                self.process_file(current_path)


# Примеры использования (наследование)
class MyWalker(BaseWalker):
    """
    Класс, который просто печатает путь текущего файла
    Смысла описывать свой конструктор, или вызывать базового класса
    нет смысла - он всё равно пустой
    """
    def process_file(self, fileName):
        """
        Переопределим функцию из BaseWalker на нужное нам поведение
        :param fileName: 
        :return: 
        """
        print('File: {} '.format(fileName))


class MySizeCalculator(BaseWalker):
    """
    Класс, подсчитывающий размер всех файлов в байтах
    , основан на BaseWalker
    (т.е. дополняет и расширяет его функциональность) 
    """
    def __init__(self):
        """
        Конструктор, вызывается при создании класса
        """
        # Мы можем вызвать конструктор базового класса
        # Хотя в нашем случае смысла мало
        # Синтаксисов вызова существует несколько
        super().__init__()
        # Сюда мы будем накапливать размер всех файлов
        # Через self мы обращаемся к функциям и переменным нашего класса
        self.__size = 0

    def process_file(self, fileName):
        """
        Переопределим функцию из BaseWalker на нужное нам поведение
        :param fileName: 
        :return: 
        """
        print('File: {} '.format(fileName))
        info = os.stat(fileName)
        self.__size = self.__size + info.st_size

    def get_size_for_all_files(self):
        """
        На терминологии getter (возвращает значение переменной класса)
        :return: 
        """
        return self.__size


# Бонус! Положим, нам нужно дополнить поведение
# walk_over_path, не повторяя её функционал:
class MyWalker2(BaseWalker):
    """
    Класс, который просто печатает путь текущего файла
    """
    def process_file(self, fileName):
        """
        Переопределим функцию из BaseWalker на нужное нам поведение
        :param fileName: 
        :return: 
        """
        print('File: {} '.format(fileName))

    def walk_over_path(self, path):
        """
        Переопределим walk_over_path
        функцию из BaseWalker на нужное нам поведение
        и вызовем walk_over_path функцию базового класса
        :param fileName: 
        :return: 
        """
        print('We process path {}'.format(path))
        # Вызовем функцию базового класса
        super().walk_over_path(path)


def main():
    path = "C:\\Users"
    # Содаём объект walker нашего класса MySizeCalculator
    # Т.е. как бы "по чертежам" MySizeCalculator
    walker = MySizeCalculator()
    walker.walk_over_path(path)
    # Сохраняю в промежуточную переменную для наглядности
    s = walker.get_size_for_all_files()
    print('All size in bytes: {}'.format(s))
    return 0


if __name__ == '__main__':
    main()
