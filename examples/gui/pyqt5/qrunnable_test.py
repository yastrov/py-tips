#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton,\
                            QWidget, QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot,\
                            QRunnable, QThreadPool, QTimer

import time
import traceback

__doc__ = '''PyQt5 QRunnable example
Based on https://mfitzp.io/article/multithreading-pyqt-applications-with-qthreadpool/
but rewritten by me.
'''


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress

    Also you can use factory like this:
    def factory(QClass, cls_name, signal_type):
        return type(cls_name, (QClass,), {'signal': pyqtSignal(signal_type)})

    MySlider = factory(QSlider, 'MySlider', int)
    self.sld = MySlider(Qt.Horizontal)
    self.sld.signal.connect(self.on_signal)
    '''
    # You cannot create signals as instance variables, they must be class attributes.
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self._args = args
        self._kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        try:
            for i in range(0, 100, 25):
                self.signals.progress.emit(i)
                time.sleep(1)
            result = 'Result from worker as str'
            self.signals.result.emit(result)  # Return the result of the processing
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        finally:
            self.signals.finished.emit()


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
        self.init_ui()

        self._threadpool = QThreadPool()
        #self._threadpool = QtCore.QThreadPool.globalInstance()
        #self._threadpool.setMaxThreadCount(2)
        print("Multithreading with maximum {} threads" .format(self._threadpool.maxThreadCount()))

        self._timer = QTimer()
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self.recurring_timer)
        self._timer.start()

    def init_ui(self):
        layout = QVBoxLayout()

        self._label = QLabel("Start")
        b = QPushButton("Start QRunnable")
        b.pressed.connect(self.start_new_runnable)

        layout.addWidget(self._label)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

    @pyqtSlot(int)
    def thread_progress_fn(self, n):
        print("{}% done".format(n))

    @pyqtSlot(object)
    def thread_print_output(self, s):
        print('Result: {}'.format(s))

    @pyqtSlot()
    def thread_complete(self):
        print("QRunnable worker COMPLETE!")

    @pyqtSlot(tuple)
    def thread_error(self, err):
        QMessageBox.warning(self, "Warning!", err[1], QMessageBox.Ok)
        print('Error {}\n{}'.format(err[1], err[2]))

    @pyqtSlot()
    def start_new_runnable(self):
        # Pass the function to execute
        worker = Worker(1, debug=True) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.thread_print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.thread_progress_fn)
        worker.signals.error.connect(self.thread_error)
        worker.setAutoDelete(True)
        # Execute (tryStart() better than start() )
        if self._threadpool.tryStart(worker) is False:
            print("Can't create worker!")
            QMessageBox.warning(self, "Warning!", "Can't create worker!", QMessageBox.Ok)

    @pyqtSlot()
    def recurring_timer(self):
        self._counter += 1
        self._label.setText("Counter: {}".format(self._counter))
        print('Active thread count: {}'.format(self._threadpool.activeThreadCount()))

    def closeEvent(self, event):
        """Main window closed, override PyQt5 widget function"""
        print('Try to exit, active thread count: {}'.format(self._threadpool.activeThreadCount()))
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self._threadpool.waitForDone()
            self._timer.stop()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
