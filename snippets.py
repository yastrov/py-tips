#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
My snippets.
Some snippets you may see at:
./core/generator.py
./core/decorator.py
"""

def mkdir(new_dir):
    """
    Create dir with name new_dir and all prev dirs.
    Equivalent for os.makedirs.
    """
    _path = os.path.dirname(new_dir)
    if os.path.exists(_path):
        return
    _p_list = []
    # Or while for raw Win path
    if _path.endswith(os.path.sep):
        _path = _path[:-1]
    while not os.path.exists(_path):
        _p_list.append(os.path.basename(_path))
        _path = os.path.dirname(_path)
    _p_list.reverse()
    while _p_list:
        _path = os.path.join(_path, _p_list.pop(0))
        os.mkdir(_path)

## Zip Reader and writer

class FilesZipReader(SimpleReader):
    def __init__(self, filename):
        self.zipfilename = zipfilename
        self.zip = zipfile.ZipFile(self.zipfilename, 'r')
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if self.zip is not None:
            self.zip.close()
        if exc_type is None:
            pass
    def get_namelist(self):
        return zip.namelist()
    def get_file(self, filename, asbinaryfile=True):
        data = self.zip.read(name)
        if asbinaryfile:
            data = BytesIO(data)
        return data
    def close(self):
        if self.zip is not None:
            self.zip.close()


class ZipWriter:
    def __init__(self, zipfilename,
                    flag=zipfile.ZIP_DEFLATED):
        self.zipfilename = zipfilename
        self.zip = zipfile.ZipFile(self.zipfilename,
                                'w', flag)
        self.flag = flag

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.zip is not None:
            self.zip.close()
        if exc_type is None:
            pass

    def write_file(self, filename, newfilename=None, compress_type=None):
        newfilename = newfilename or os.path.basename(filename)
        compress_type = compress_type or self.flag
        self.zip.write(filename, newfilename,
                        compress_type=compress_type)

    def write_str(self, data, newfilename, compress_type=None):
        compress_type = compress_type or self.flag
        self.zip.writestr(newfilename, data,
                            compress_type=compress_type)

    def close(self):
        if self.zip is not None:
            self.zip.close()


class EpubWriter(ZipWriter):
    """EpubWriter"""
    def __init__(self, bookname):
        super(ZipWriter, self).__init__(bookname)
    def __walk(self, path):
        for base, dirs, files in os.walk(path):
            for fname in files:
                yield os.path.join(base, fname)
    def compile(self, path):
        self.write_str('application/epub+zip', 'mimetype',
                        compress_type=zipfile.ZIP_STORED)
        for name in self.__walk(path):
            if name is 'mimetype':
                continue
            new_name = name.replace(path, '')
            self.write_file(name, new_name,
                            compress_type=zipfile.ZIP_DEFLATED)
