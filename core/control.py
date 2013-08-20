#!/usr/bin/env python3
#encoding: utf-8

__doc__ = """Control of execution. Tips.

help(object) - справка по объекту или модулю. Для выхода из справки нажать клавишу 'q'
dir(object) - список методов и переменных объекта (так же и класса и модуля) в виде словаря.
id(object) - адрес объекта в памяти.

!строки не изменяемы!
"""

#If and None problem
n = None
if n is None:
    #Only None here
    pass
elif n:
    #Equivalent of n == True
    #also n may be is any existing object
    pass
elif not n:
    #Equivalent of n == False
    pass
else:
    pass

# Именно такие проверки с not
if n is not None:
    #Any value without None: True, False, 1, ...
    #Also in some context, False may be return.
    pass

if n not in [1,2]:
    pass

i = 5
# использовать скобки запрещено!
if 1 < i < 10:
    pass

#Logick operators: and, or
#return type of one from operator.
t = type(3 or 'a')
print("3 or 'a' have type %s" %t)

#Loops
while True:
    pass

i = 0
while i < 10:
    print(i)
    i +=1

for el in [1, 2, 3]:
    print(el)

if __name__ == '__main__':
    pass
