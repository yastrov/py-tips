#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    ABC позволяют определить класс, указав при этом, какие методы или свойства обязательно переопределить в классах-наследниках:
    Примеры взяты из: http://habrahabr.ru/post/72757/
"""
from abc import ABCMeta, abstractmethod, abstractproperty

class Pressable(metaclass=ABCMeta):
    #__metaclass__ = ABCMeta

    @abstractmethod
    def press():
        """Нажать на объект"""
    
    @abstractproperty
    def depth():
        """Глубина нажатия у объекта"""


class Button(Pressable):
    def __init__(self):
        self.__depth = 7

    def press(self):
        pass
        
    def get_depth(self):
        return self.__depth

    def set_depth(self, val):
        self.__depth = val
    depth = property(get_depth, set_depth)

assert issubclass(Button, Pressable)
assert isinstance(Button(), Pressable)

info = """For creating class, similar for
builtins classes, based on abstract containers:
https://docs.python.org/dev/library/collections.abc.html#module-collections.abc
http://asvetlov.blogspot.ru/2014/09/abstract-containers.html
"""