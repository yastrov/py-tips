#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import os

def pack_path_to_zip(zip_path, path):
    """Запаковать путь, директорию"""
    assert(isinstance(zip_path, str), 'Argument zip_path must be an str.')
    assert(isinstance(path, str), 'Argument path must be an str.')
    # path must be exists and be a folder
    if not os.path.exists(path) or not os.path.isdir(path):
        print('Folder: {} does not exists!'.format(path))
        return
    # For speed and short code
    join = os.path.join
    relpath = os.path.relpath

    with zipfile.ZipFile(zip_path, 'w',
                         zipfile.ZIP_DEFLATED, False) as myzip:
        for root, dirs, files in os.walk(path):
            for file in files:
                _path = join(root, file)
                # For subfolder with plugin name in ZIP
                _inner_path = join(plugin_name, relpath(_path, path))
                myzip.write(_path, _inner_path)


if __name__ == '__main__':
    pack_path_to_zip('C:\\my_zip.zip', 'C:\\my_folder')
