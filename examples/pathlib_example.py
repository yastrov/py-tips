#!/usr/bin/env python3
#encoding: utf-8
from pathlib import Path
# Recursively 'glob' all files under the current directory
# See also docs or dir(Path)
for path in Path('.').rglob('*.*'):
    print('->', path)
    print('File name:', path.name)
    print('Suffix:', path.suffix)
    print('Absolute path as str:', path.resolve())