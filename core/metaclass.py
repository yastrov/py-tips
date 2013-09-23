#!/usr/bin/env python3
# encoding: utf-8

__doc__ = """Basic Metaclass.
"""

class MyMeta(type):

    # The prepare function
    @classmethod
    def __prepare__(metacls, name, bases): # No keywords in this case
        return dict() #Or any class based on dict()

    # The metaclass invocation
    def __new__(cls, name, bases, classdict):
        # Note that we replace the classdict with a regular
        # dict before passing it to the superclass, so that we
        # don't continue to record member names after the class
        # has been created.
        print("Bases:\n%s" %bases)
        print("Dict:")
        pprint(classdict)
        classdict["say_hello"] = lambda self: print("Hello")
        result = type.__new__(cls, name, bases, dict(classdict))
        result.member_items = classdict.items()
        return result


class MyClass(metaclass=MyMeta):
    def method1(self):
        pass

if __name__ == '__main__':
    m = MyClass()
    print(m.member_items)
    m.say_hello()
