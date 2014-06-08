#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """
Glue txt files to one.
"""
from glob import glob
import traceback

def glue_files(f_list, resultfname):
    import fileinput
    flag = False
    try:
        with open(resultfname, 'wb') as fout,\
            fileinput.input(files=f_list, mode='rb') as fin:
                for line in fin:
                    if flag and fin.isfirstline():
                        fout.write(b'\n')
                    flag = True
                    fout.write(line)
                    prev = fin.fileno()
    except (IOError, OSError) as e:
        print(e)
        traceback.print_stack()

def inter(x):
    y = x.split('.')[0]
    return int(y)

def filter_int_names(fname):
    import string
    name = fname.split('.')[0]
    for char in name:
        if char not in string.digits:
            return False
    return True

if __name__ == '__main__':
    import sys
    file_name = 'result.txt'
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        if file_name in ['-h', '--help']:
            print('Usage: %s result-filename' %sys.argv[0])
            print('\n\n%s' %__doc__)
            exit()

    f_list = glob('*.txt')
    f_list= list(filter(filter_int_names, f_list))

    f_list.sort(key=inter)
    glue_files(f_list, file_name)
