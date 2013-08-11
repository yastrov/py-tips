#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """With statement.
with позволяет:
* исполнить код до начала блока
* исполнить код по выходу из блока, 
    независимо от того это выход по исключению 
    с помощью return или другим способом
* обработать исключение, возникшее в блоке.

Замена конструкции вида:
obj = Wrapper()
obj.__enter__()
try:
    #действие с obj
finally:
    #освобождение ресурсов
    obj.__exit__()
    
Применение:
with Wrapper() as obj:
    #do somthing with obj here
    print(repr(obj))

For example:
with open(filename, 'r') as f:
    data = f.read()
#There is no need in f.close()

Смотри: http://koder-ua.blogspot.ru/2011/12/with.html
http://www.python.org/dev/peps/pep-0343/
"""

class Wrapper:

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        """Подготовка к действию"""
        return self.obj
        #В принципе, можно добавить интерфейс with-а
        #к самому obj. Тогда будет:
        #return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Освобождает ресурсы. Вызывается в любом случае.
        (В "классическом" коде вызывался бы по finally)
        Например:
        return isinstance(value, TypeError)
        подавит исключения TypeError, вернув True"""
        if exctype is None:
            #All Ok, no Exceptions
            pass
        else:
            print(exc_value)
        # For example without check for self.obj exists
        self.obj.close()


if __name__ == '__main__':
    filename = input('Enter filename: ')
    f = open(filename, 'r')
    with Wrapper(f) as obj:
        data = f.read()
        print(data)
