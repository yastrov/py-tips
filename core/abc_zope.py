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

###
import zope.interface

class IVehicle(zope.interface.Interface):
    """Any moving thing"""
    speed = zope.interface.Attribute("""Movement speed""")
    def move():
        """Make a single step"""
    
class Car(object):
    zope.interface.implements(IVehicle)

    def __init__:
        self.speed = 1
        self.location = 1

    def move(self):
        self.location = self.speed*1
        print "moved!"
    
assert IVehicle.implementedBy(Car)
assert IVehicle.providedBy(Car())
