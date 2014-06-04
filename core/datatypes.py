#!/usr/bin/env python
#encoding: utf-8

__doc__ = """Basic datatypes.
"""

#Only for example.
#For more information see documentation.
t = True
t = False
n = None

f = float("6.8")
f = 6.8

i = int(f)
i = 6
i = int('0xA6F', 16) #from hex, base=16
print(hex(i))
################################
#Turple
#uneditable, unchangeable
data = (1, 2, 3)

################################
print("# List")
l = list() # l = []
l = [[] for _ in range(5)]
l = ['1', '2', '3', '4'] # list
print(dir(l)) #What methods are exists
l1 = l[:] # Slice, copy of list
print('l: %s' %l)
print('l[2]: %s' %l[2])
print('l[2:]: %s' %l[2:])
print('l[1:3]: %s' %l[1:3])
print('l[-2]: %s' %l[-2])
l[::2]  # Указываем шаг
a[::-1] # Переворачиваем (reverse) список
zip(l[::2], l[1::2])
d = {k: v for k,v in zip(l[::2], l[1::2])}

if '1' in l:
    print("list has element '1'")
#map object is iterator
l_int = list(map(int, l))
for el in map(lambda x: x**2, l_int):
    print(el)

foo = lambda x: True if x > 2 else False
#filter object is iterator
#l3 = list(filter(foo, l_int))
for el in filter(foo, l_int):
    print(el)

r = [x**2 for x in range(10) if x % 2 == 0]
print(min(r), max(r))
r[:5] = [42] # Все символы до 5 заменяются элементом "42"
del r[::2] # Удаление каждого второго элемента

r = zip([1, 2, 3], [4, 5, 6])
print(r)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
r = sorted(seasons, key=len)
print(r) #Sort list by len() function
r = ','.join(seasons) # ->string
print(r)

#list -> generator -> list
r = list(enumerate(seasons))
print(r)

l = [False, True, False]
r = any(l)
print(r)
r = all(l)
print(r)

l = [b for a in A for b in B]
#Is equivalent to:
l = []
for a in A:
  for b in B:
    l.append(b)

################################
print("# Dict")
a = dict()
a = {'zero':0, 'one':1}
b = {}.fromkeys(['1','2','3','4'], 1)
c = b['1']
b['1'] = 2
b = {x:x**3 for x in range(1, 4)}
# AT!
a = { ('one', '1'): 1, ('two', '2'): 2 }
print( a['one', '1'] ) 
#Слияние двух списков в словарь:
t1 = (1, 2, 3)
t2 = (4, 5, 6)
b = dict (zip(t1,t2))

#Следующий get работает быстрее
#и без Exception
#при отсутствии элемента в словаре
c = a.get('count', None)
if c is not None:
    print('dict contain "count" key:')
    print(c)
else:
    print('no "count" key in dict')

print(a.keys())
print(a.values())
print(a.items())

################################
print("# String")
s = "Hello world.\n" #Сам по себе объект string не изменяемый.
print( hex(ord(s[0])) )
print(dir(s)) # For all functions
s = s.rstrip() # обрезает конец строки справа: \n, \r\n
#see also: st.strip(),  chr(), ord()
l = s.split() # split(delimeter): string -> list
s = s*3 # строка из 3х строк s
if "w" in s:
    print("W in s string")
#Encode
encoding = 'utf-8'
r = s.encode('ascii', 'ignore') #ignore, replace, strict, xmlcharrefreplace
print(r)
try:
    r = s.decode('utf-8', 'ignore')
    print(r)
except AttributeError as e:
    print(e)
r = b'hello'.decode(encoding)
print(r)
r = str(b'hello', encoding)
print(r)
unicode_string = s.encode(encoding)

#bytes -> str
if isinstance(s, bytes) and bytes([10]) in s:
    s = s.decode("utf-8")
#str -> bytes
if isinstance(s, str):
    s = s.encode("UTF-8")

#lower all
s = 'start TT end AAA BBBBBBB'
for c in s:
    if c.isupper():
        s = s.replace(c,c.lower())
print(s)

## START
# Or eq
def oper(func, iterables):
    l = map(func, iterables)
    return ''.join(l)
 
def foo(char):
    if char.isupper():
        return char.lower()
    else:
        return char

s = oper(foo, 'My homeworld')
### END

#Old style
message = '%s : %s' %('Alice','hash')
#New style format string
message = '{Name:s} : {hashValue:s}'
table = {'Name': 'Alice', 'hashValue': 'hash'}
mes = message.format(**table)

################################
print("# Set")
varSet = {1, 2, 3, 4, 5}
my_set = {i ** 2 for i in range(10)}
print(type(varSet))
print(2 in varSet)
varSet | my_set # Объединение
varSet & my_set # Пересечение
varSet < my_set # Подмножества
varSet - my_set # Разница
varSet ^ my_set # Исключающее или (XOR)
# Exist unchangeable version: frozenset
################################
print("# Decimal")
#Decimal (Например для валют)
from decimal import Decimal, getcontext
#Точность 3 знака, против 28 стандартных
getcontext().prec = 3
d = Decimal("4.31")
print(d / 3)
#Правила округления тоже задаются контекстом.
from decimal import Context, localcontext
with localcontext(Context(4)):
    print(repr(Decimal("1.10") / 3))
d = Decimal('1.12').quantize(Decimal('0.1'))

################################
print("# Fraction")
#Fraction - Предназначен для работы с обыкновенными дробями
#http://python-history.blogspot.com/2009/03/problem-with-integer-division.html
#http://asvetlov.blogspot.ru/2012/08/numerics.html
from fractions import Fraction
Fraction(7, 71) * 71 == 7

################################
#Bytes - unchangeable
b1 = b'hello'
b2 = 'Привет'.encode('utf-8')
ub2 = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode('utf-8')
b3 = bytes('hello', encoding = 'utf-8')

#changeable version:
b = bytearray(b'hello world!')
result = bytearray.fromhex('deadbeef')

from collections import OrderedDict, namedturple
# OrderedDict сохраняет порядок ключей
d = {'zero':0, 'two':2 ,'one':1}
ordered_d = OrderedDict(sorted(d.items(), key=lambda x: x[0]))
# namedturple ведёт себя как кортеж. Возможно
# использовать в качестве структуры вместо класса.
Point = namedtuple('Point', ['x', 'y'])
p = point(x=1, y=2)
print(p.x)
print(p[0])
