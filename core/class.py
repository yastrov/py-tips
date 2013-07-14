#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Class examples, snippets.
"""

class A:
    """Class A example."""
    x = 5

    def __init__ (self):
        #super(A, self).__init__()
        # Initialization
        pass

    def __getattr__(self, name):
        """Is called to get attributes that 
        cannot be found using the standard 
        attribute lookup algorithm. """
        print("__getattr__: {}".format(name))
        return None

    def __setattr__(self, name, value):
        print("__setattr__: {}".format(name))
        self.__dict__[name] = value

    def __repr__ (self):
        """Представление для вывода"""
        return '<{}.{} object at {}>'.format(
                self.__class__.__module__,
                self.__class__.__name__,
                hex(id(self)) )

    def __str__ (self): pass

    #Деструктор
    #def __del__(self): pass

    @staticmethod
    def f():
        """Static, создание экземпляра класса
        не требуется, потому нет self.
        Вызов: A.f()"""
        pass

    @classmethod
    def f2(cls):
        """Модификация аттрибутов самого класса"""
        cls.x = 4

    def foo(self):
        print('Hello!')

    def __call__(self):
        """Пример:
        a = A()
        a()"""
        pass


class B(A):
    def __init__(self, arg):
        super(B, self).__init__()
        self.arg = arg

    def getX(self):
        return self.x

    def setX(self, value):
        self.x = value


class Account:
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError('Invalid email address.')
        self._email = value


if __name__ == '__main__':
    a = A()
    print(type(a))
    print(isinstance(a, A))
    a.y = 8
    el = a.y
    el =  a.z #We have no 'z' in class A
    print(a.y) #Without call any 'get'. ()
    try:
        print(dir(a))
    except TypeError as e:
        print('Please, use Python 3.3, or inherit A from object: A(object)')
    print('a.__dict__:\n{}'.format(a.__dict__) )
    #result: {'y': 8}
    print('A.__dict__:\n{}'.format(A.__dict__) )
    #A.__dict__ == type(a).__dict__
    #print(help(a)) #'help' present summary __doc__ of class
    print('a.__doc__:\n{}'.format(a.__doc__))
    if hasattr(a, 'foo'):
        print('"a" has attribute: foo')
        a.foo()

    a = Account()
    try:
        a.email = 'badaddress'
    except ValueError as e:
        print("Invalid email value!")

    # Attention! It is bad practice!
    # Modification of the class while the script work.
    l = lambda self: print("It is new function: say_hello!")
    A.say_hello = l
    a.say_hello()
    type(a).say_h = lambda self: print("It is say_h!")
    a.say_h()