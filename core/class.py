#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Class examples, snippets.

Доступ к свойству, находящемуся в словаре класса происходит дольше, чем
к свойству в словаре инстацированного объекта.

Also you may read http://habrahabr.ru/post/186608/

Please, read the article about override operation.
For example Point class:
http://asvetlov.blogspot.ru/2014/09/magic-methods.html
"""

class A:
    """Class A example."""
    x = 5 # доступ к переменной класса дольше, чем к меременной объекта.
    # __slots__ = ("x",) # May safe RAM for very much instances. x - variable

    def __init__(self):
        #super(A, self).__init__()
        #super().__init__()
        # Initialization
        pass

    def __getattr__(self, name):
        """Is called to get attributes that 
        cannot be found using the standard 
        attribute lookup algorithm. """
        print("__getattr__: {}".format(name))
        return None
        
    #def __getattribute__(self, keyy):
    #    """Call only for exists attributes.
    #    for new-style classes only.
    #    if you define both, __getattr__ will not be called.
    #    http://www.devx.com/opensource/Article/31482/0/page/4 
    #    """
    #    return key

    def __setattr__(self, name, value):
        print("__setattr__: {}".format(name))
        #super().__setattr__(name, value)
        self.__dict__[name] = value

    def __repr__(self):
        """Представление для машинно-ориентированного вывода"""
        return '<{}.{} object at {}>'.format(
                self.__class__.__module__,
                self.__class__.__name__,
                hex(id(self)) )

    def __str__(self): return super().__str__();

    #def __dir__(self): pass

    #Деструктор
    #def __del__(self): pass
    # Do not overload this: GC may not collect that class

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

    @classmethod
    def from_file(cls, fname):
        data = None
        with open(fname, "r") as f:
            data = f.read()
        return cls(data)

    def foo(self):
        print('Hello!')

    def __call__(self):
        """Пример:
        a = A()
        a()"""
        pass

    def __getitem__(self, key):
        """a['mykey']"""
        return self.__dict__[key]
    #def __setitem__(self, key, value)

class B(A):
    def __init__(self, arg=None):
        super(B, self).__init__()
        self._x = arg

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    x_wrap = property(get_x, set_x)
    #b = B()
    #b.x_wrap = 7
    #b.x_wrap
    
    #Call parent method
    def __setitem__(self, key, value):
        #A.__setitem__(self, key, value)
        super(B, self).__setitem__(key, value)
        # Or New for Python 3.3
        super().__setitem__(key, value)

    def foo(self):
        """Method Overriding in Python"""
        # Before or after local code
        super().foo()

class Account:
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError('Invalid email address.')
        self._email = value
        
    @email.deleter
    def email(self):
        del self._email
    #email = property(_getter, _setter, _deleter, "doc string")


# Descriptor version
class Descriptor:
    def __init__(self, val=None):
        self._v  = val
    def __get__(self, obj, type):
        print("getter used")
        return self._v
    def __set__(self, obj, val):
        print("setter used")
    def __delete__(self, obj):
        print("deleter used")
        del self._v


class Account2:
    email = Descriptor()


if __name__ == '__main__':
    a = A()
    print(type(a))
    print(isinstance(a, A))
    print(issubclass(B, A))
    a.y = 8 #setattr(a, 'y', 8)
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
    x = getattr(a, 'x', None)

    ac = Account()
    try:
        ac.email = 'badaddress'
    except ValueError as e:
        print("Invalid email value!")

    # Attention! It is bad practice!
    # Modification of the class while the script work.
    l = lambda self: print("It is new function: say_hello!")
    A.say_hello = l
    a.say_hello()
    type(a).say_h = lambda self: print("It is say_h!")
    a.say_h()
