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

# Copy to previous for previous folder
from shutil import move, copy
root_dir = ''
#dest_dir = ''
src = Path(root_dir)
#dest = Path(dest_dir)
for file in src.rglob('*.jpg'):
    dest = file.absolute().parent.parent
    #dest_file = dest / file.relative_to(src)
    dest_file = dest / file.name
    try:
        if not dest_file.parent.exists():
            dest_file.parent.mkdir(parents=True)
    except OSError as e:
        print(e)
    #move(str(file), str(dest_file))
    copy(str(file), str(dest_file))