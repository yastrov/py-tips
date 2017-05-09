#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton,\
                            QWidget, QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot, QTimer


__doc__ = '''PyQt5 Timer example'''

class MainWindow(QMainWindow):
    """
    You can use @pyqtSlot(int) syntax (with parameters), or you can pass this,
    but it make code more readable.
    Вы можете использовать синтаксис объявления слотов @pyqtSlot(int)
    с указанием типа передаваемых значений, или опустить его вовсе,
    однако это делает код нагляднее
    и позволяет быстро понять, что слот, а что - функция.
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self._counter = 0
        # Создаём таймер и присваиваем в локальную переменную класса
        self._timer = QTimer()
        # Задаём интервал в милисекундах
        self._timer.setInterval(1000)
        # Подсоединяем слот, куда таймер будет слать сообщения
        self._timer.timeout.connect(self.recurring_timer)

        # Вызываем функцию настройки внешнего облика
        # Такая последовательность потому,
        # что мы будем прикреплять кнопки к таймеру,
        # а для этого он должен быть создан
        self.init_ui()
        # Можно и вначале кнопки, а таймер потом, но чуть больше кода и меньше наглядности
        # Запуск таймера
        self._timer.start()

    def init_ui(self):
        # Штука, в которой мы будем располагать кнопки, надписи и т.п.
        # В названии QVBoxLayout есть V от Vertical
        layout = QVBoxLayout()
        # Создадим надпись
        self._label = QLabel("Start")
        layout.addWidget(self._label)

        button_stop = QPushButton("Stop timer")
        # Подключаем кнопку напрямую к слоту таймера "остановить"
        # Кнопка будет при нажатии посылать сообщения "на адрес" self.self._timer.stop
        button_stop.clicked.connect(self._timer.stop)
        layout.addWidget(button_stop)

        button_start = QPushButton("Start timer")
        # Подключаем кнопку напрямую к слоту таймера "запуск"
        button_start.clicked.connect(self._timer.start)
        layout.addWidget(button_start)

        # Создаём виджет пустышку,
        # чтобы разместить на нём layout спасибо за это QMainWindow-у
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    @pyqtSlot()
    def recurring_timer(self):
        self._counter += 1
        self._label.setText("Counter: {}".format(self._counter))

    def closeEvent(self, event):
        """Вызывается, когда мы закрываем окно.
        Вызов этой функции обеспечивает сам QMainWindow"""
        # Зададим пользователю вопрос
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            # Пользователь сказал "да, хочу выйти"
            self._timer.stop()
            # Одобряем выход
            event.accept()
        else:
            # отменяем запрос на выход
            event.ignore()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


