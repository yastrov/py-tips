#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    ABC позволяют определить класс, указав при этом, какие методы или свойства обязательно переопределить в классах-наследниках:
    Примеры взяты из: http://habrahabr.ru/post/72757/
"""

from abc import ABCMeta, abstractmethod, abstractproperty

class Movable(metaclass=ABCMeta):
    #__metaclass__ = ABCMeta

    @abstractmethod
    def move():
        """Переместить объект"""
    
    @abstractproperty
    def speed():
        """Скорость объекта"""


class Car(Movable):
    def __init__(self):
        self.speed = 10
        self.x = 0
    def move(self):
        self.c += self.speed
    def speed(self):
        return self.speed

assert issubclass(Car, Movable)
assert isinstance(Car(), Movable)
