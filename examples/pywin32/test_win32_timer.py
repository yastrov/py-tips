# -*- coding: utf-8 -*-
"""
Обёртка над Windows API под названием pywin32.
Официальная страница проекта https://sourceforge.net/projects/pywin32/

Но устанавливать лучше через pip
pip install pypiwin32

Полный вызов pip для Python 3.6 через CMD.exe:
%LOCALAPPDATA%\Programs\Python\Python36\python -m pip pypiwin32
-----------
pywin32 содержит в себе несколько модулей, в том числе:
win32api
timer
Названия всех модулей http://timgolden.me.uk/pywin32-docs/win32_modules.html
--------------------
Более сложный пример смотри:
https://github.com/arizvisa/pywin32/blob/windows-219/win32/Demos/timer_demo.py

Вывод получился:
my_callback 9568 time=158382468
my_timer_id == timer_id True
my_callback 9568 time=158382578
my_timer_id == timer_id True
my_callback 9568 time=158382687
my_timer_id == timer_id True
my_callback 9568 time=158382796
my_timer_id == timer_id True
    
"""
import timer

# Глобальные переменные скрипта
my_timer_id = 0 # Уникальный идентификатор таймера, пока просто объявим имя
my_millisecundes_interval = 100 # Интервал в милисекундах
counter = 0 # счётчик тиков (срабатываний) таймера

def my_callback(timer_id, time):
    """Наша функция, которую вызовет таймер"""
    # Выведем информацию. print можно написать по разному.
    # Здесь вначале создадим строку 'my_callback {} time={}' в которую с помощью
    # format подставим два значения на место значков {}
    # format - функция присущая текстовым строкам
    # получившуюся после подстановки значений строку отправим print-у
    print('my_callback {} time={}'.format(timer_id, time))
    # В выводе можем заметить, что все выведенные time отличаются почти на 100
    global my_timer_id # Явно показываем, что берём глобальную переменную
    print('my_timer_id == timer_id {}'.format(my_timer_id == timer_id))
    # как мы увидим, идентификаторы имеют одинаковое значение.
    global counter # Явно показываем, что берём глобальную переменную,
    # вдруг новую локальную создаст, или упадёт
    counter = counter + 1
    # После 4-го срабатывания остановим таймер и удалим из ОС
    if counter == 4:
        # Останавливаем таймер.
        timer.kill_timer(timer_id)

# Создадим таймер, с интервалом и функцией обратного вызова.
# Сам таймер создастся где-то в недрах ОС, мы получим только его идентификатор (номер) в my_timer_id
my_timer_id = timer.set_timer(my_millisecundes_interval, my_callback)
# И сразу после создания пошли выполняться дальше
if my_timer_id == 0:
    print('Не удалось создать тааймер!')
print(type(my_timer_id))
# Нужно обязательно остановить таймер, иначе он останется работать.
# Здесь мы этого сделать не можем: сюда мы проскочим ещё
# до первого вызова my_callback и вессь смысл потеряется
# Поэтому нужно либо писать сложную обёртку (в большой сложной программе)
# или удалять в самом my_callback
