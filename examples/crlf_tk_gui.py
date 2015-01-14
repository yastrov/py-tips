#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.filedialog as tkfd
import tkinter.messagebox as msgbox
import os
import weakref

"""Universal utility for work (detect and edit) with CRLF and LF line endings.

Why in one file? Because it is helpfull utility, not big project.

Written for Python 3.*"""
__about__ = "Universal utility for work with CRLF and LF line endings."
__version__ = "1.0.0"

ReferenceType = weakref.ReferenceType

try:
    from enum import Enum as EnumParent
except ImportError:
    EnumParent = object

class WorkerCommand(EnumParent):
    COMMAND_TEST = 1
    COMMAND_TO_CRLF = 2
    COMMAND_TO_LF = 3
    COMMAND_CRLF_FIX_END = 4

class Worker:
    CRLF_NAME = "CRLF"
    CRLF_DATA = b"\r\n" # bytes([0x0D,0x0A,])
    LF_DATA = b"\n" # bytes([0x0A,])
    LF_NAME = "LF"

    def __init__(self, printer):
        self._printer = printer
        self._command = None

    def print_func(self, msg):
        if isinstance(self._printer, ReferenceType):
            self._printer().print_func(msg)
        else:
            self._printer.print_func(msg)

    def _walk(self, path):
        """
        Walk on path.
        """
        pjoin = os.path.join
        for base, dirs, files in os.walk(path):
            for _file in files:
                yield pjoin(base, _file)

    def single_file_test(self, filename):
        end = 'Unknown'
        try:
            with open(filename, "rb") as f:
                data = f.read()
                if Worker.CRLF_DATA in data:
                    end = Worker.CRLF_NAME
                elif Worker.LF_DATA in data:
                    end = Worker.LF_NAME
                else:
                    end = data[-2:]
            self.print_func("{} has at end: {}".format(filename, end))
        except PermissionError as e:
            self.print_func("Permission denied to file: {}".format(filename))
            end = 'Unknown'
        finally:
            return end

    def _single_file_rewrite(self, filename, from_end, to_end):
        data = None
        try:
            with open(filename, "rb") as f:
                data = f.read()
            with open(filename, "wb") as f:
                data = data.replace(from_end, to_end)
                f.write(data)
                CRLF_DATA = Worker.CRLF_DATA
                if to_end == CRLF_DATA\
                    and data[-2:] != CRLF_DATA:
                    f.write(CRLF_DATA)
            self.print_func('{}: Converted'.format(filename))
        except PermissionError as e:
            self.print_func("Permission denied to file: {}".format(filename))
        except Exception as e:
            self.print_func(e)

    def single_file_crlf_fix(self, filename):
        data = None
        CRLF_DATA = Worker.CRLF_DATA
        #double_CRLF_DATA = b''.join((CRLF_DATA,CRLF_DATA))
        double_CRLF_DATA = b'\r\n\r\n\r\n'
        try:
            with open(filename, "rb") as f:
                data = f.read()
            if data.count(double_CRLF_DATA) > 6:
                data = data.replace(double_CRLF_DATA,
                                    CRLF_DATA)
            with open(filename, "wb") as f:
                f.write(data)
                if data[-2:] != CRLF_DATA:
                    f.write(CRLF_DATA)
            self.print_func('{}: Fixed'.format(filename))
        except PermissionError as e:
            self.print_func("Permission denied to file: {}".format(filename))
        except Exception as e:
            self.print_func(e)

    def single_file_to_LF(self, filename):
        self._single_file_rewrite(filename,
                                    Worker.CRLF_DATA,
                                    Worker.LF_DATA)

    def single_file_to_CRLF(self, filename):
        self._single_file_rewrite(filename,
                                    Worker.LF_DATA,
                                    Worker.CRLF_DATA)

    def single_file_process(self, filename, command=None):
        """
        Recomended function for work with one file.
        command must be a type of WorkerCommand
        """
        if command is not None: self._command = command
        if self._command == WorkerCommand.COMMAND_TEST:
            self.single_file_test(filename)
        elif self._command == WorkerCommand.COMMAND_TO_CRLF:
            self.single_file_to_CRLF(filename)
        elif self._command == WorkerCommand.COMMAND_TO_LF:
            self.single_file_to_LF(filename)
        elif self._command == WorkerCommand\
                                    .COMMAND_CRLF_FIX_END:
            self.single_file_crlf_fix(filename)
        else:
            self.print_func('WorkerCommand: {}'.format(command))
            raise NotImplementedError(\
                'Worker.single_file_process has no command!')

    def single_path_process(self, path):
        if os.path.isdir(path):
            _sfp = self.single_file_process
            for fname in self._walk(path):
                _sfp(fname) 
        elif os.path.isfile(path):
            self.single_file_process(path)

    def main_process(self, path, command=None):
        """
        Main function for process path and execute command.
        command must be a type of WorkerCommand
        """
        if command is not None:
            self._command = command
        if isinstance(path, (list, tuple)):
            for p in path:
                self.single_path_process(p)
        else:
            self.single_path_process(path)


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.initial_dir = os.getcwd()
        self.worker = Worker(printer=weakref.ref(self))

        def show_error(*args):
            import traceback
            a = traceback.format_exception(*args)
            msgbox.showerror(a[-1], "\n".join(a[:-1]))        
        self._root().report_callback_exception = show_error

    def create_widgets(self):
        button_main_row = 1
        self.label = tk.Label(self, text=__about__)
        self.label.grid(row=0, columnspan=6)
        # Row 1
        self.test_file_button = tk.Button(self,
                                          text="Scan file",
                                          command=self.test_file)
        self.test_file_button.grid(row=button_main_row, column=0)
        self.test_folder_button = tk.Button(self,
                                          text="Scan folder",
                                          command=self.test_folder)
        self.test_folder_button.grid(row=button_main_row, column=1)
        self.file_to_CRLF_button = tk.Button(self,
                                             text='File to CRLF',
                                             command=self.file_to_CRLF)
        self.file_to_CRLF_button.grid(row=button_main_row, column=2)
        self.file_to_LF_button = tk.Button(self,
                                           text='File to LF',
                                           command=self.file_to_LF)
        self.file_to_LF_button.grid(row=button_main_row, column=3)
        self.folder_to_CRLF_button = tk.Button(self,
                                               text="Folder to CRLF",
                                               command=self.folder_to_CRLF)
        self.folder_to_CRLF_button.grid(row=button_main_row, column=4)
        self.folder_to_LF_button = tk.Button(self,
                                            text="Folder to LF",
                                            command=self.folder_to_LF)
        self.folder_to_LF_button.grid(row=button_main_row, column=5)
        #Row 2
        self.file_fix_CRLF_button = tk.Button(self,
                                                text="Fix CRLF file",
                                                command=self.file_CRLF_file_fix)
        
        self.file_fix_CRLF_button.grid(row=button_main_row+1, column=0)
        self.folder_fix_CRLF_button = tk.Button(self,
                                                text="Fix CRLF folder",
                                                command=self.folder_CRLF_file_fix)
        self.folder_fix_CRLF_button.grid(row=button_main_row+1, column=1)
        # Row 3 Text Field
        self.sc_text = scrolledtext.ScrolledText(self)
        self.sc_text.grid(row=button_main_row+2, columnspan=6)
        # Row 4
        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                command=self.master.destroy)
        self.QUIT.grid(row=button_main_row+3, columnspan=6)

    def msgbox(self, msg):
        msgbox.showinfo("Info", msg)

    def print_func(self, msg):
        self.sc_text.insert(tk.END, msg+'\n')

    def _get_filename(self):
        options = {}
        options['defaultextension'] = '.*'
        options['filetypes'] = [('all files', '.*'), 
                                ('text files', '.txt'),
                                ('Python files', '.py')]
        options['initialdir'] = self.initial_dir
        #options['initialfile'] = 'myfile.txt'
        options['parent'] = self
        options['title'] = 'Choose a file'
        filename = tkfd.askopenfilename(**options)
        self.initial_dir = os.path.dirname(filename)
        return filename

    def _get_folder(self):
        dirname = tkfd.askdirectory(parent=self,
                                    title='Choose a directory',
                                    initialdir=self.initialdir)
        self.initial_dir = dirname
        return dirname

    def test_file(self):
        self.worker.single_file_test(self._get_filename())

    def test_folder(self):
        self.worker.main_process(self._get_folder(),
                                    WorkerCommand.COMMAND_TEST)
        self.print_func('Complete!')

    def file_to_CRLF(self):
        self.worker.single_file_to_CRLF(self._get_filename())

    def file_to_LF(self):
        self.worker.single_file_to_LF(self._get_filename())

    def folder_to_CRLF(self):
        self.worker.main_process(self._get_folder(),
                                    WorkerCommand.COMMAND_TO_CRLF)
        self.print_func('Complete!')

    def folder_to_LF(self):
        self.worker.main_process(self._get_folder(),
                                    WorkerCommand.COMMAND_TO_LF)
        self.print_func('Complete!')

    def file_CRLF_file_fix(self):
        self.worker.single_file_crlf_fix(self._get_filename())

    def folder_CRLF_file_fix(self):
        self.worker.main_process(self._get_folder(),
                                    WorkerCommand.COMMAND_CRLF_FIX_END)

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.master.title(__about__)
    app.mainloop()

if __name__ == '__main__':
    main()
