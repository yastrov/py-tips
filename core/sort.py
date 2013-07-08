#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Sorted examples, snippets.
"""

def sortlist(lst, reverse=False):
    """Sort list [(,),(,)] by second element of inner turple.
    Example of list: [('three',3),('one',1),('two', 2)]"""
    foo = lambda x: x[1]
    return sorted(lst, key=foo, reverse=reverse)

def dictsort(dict_, reverse=False):
    """Alphabet sort dict by keys and return sorted list of their values.
    It have been another task, I made some changes."""
    foo = lambda x: x[0]
    list_ = sorted(dict_.items(), key=foo, reverse=reverse)
    return [x[1] for x in list_]

if __name__ == '__main__':
    lst_ = [('three',3),('one',1),('two', 2)]
    r = sortlist(lst_)
    print(r)
    data_dict = {'three': 3, 'one': 1, 'two': 2}
    print(data_dict.items())
    r = dictsort(data_dict)
    print(r)