#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Try... except examples, snippets.
See http://asvetlov.blogspot.ru/2012/12/exceptions.html
"""

#It only for example try...except using.
#Use snippet for work with sockets, thread locks and others.
#Use with statement for work with real file:
#>>> with open(...) as f:
#>>>    data = f.read()

class MyFileException(Exception): pass

filename = '/etc/hostsg'
try:
    f = open(filename, "r", encoding="utf-8") #Use codecs.open in Python before 3.3
    try:
        data = f.read()
        print(data)
    finally:
        f.close()
except FileNotFoundError as ex:
    pass
except PermissionError as ex:
    pass
except OSError as ex:
#except (os.error, IOError) as ex: #For before Python 3.3
    raise MyFileException(filename) from ex #Цепочки искючений. Начиная с версии 3.3