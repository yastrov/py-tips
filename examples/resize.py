#!/usr/bin/env python3
#encoding: utf-8
"""
Resize images to 888x888 (for diary.ru)
Install PILLOW for Python 3 on Windows
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow

download Python from https://www.python.org/downloads/
"""
from PIL import Image
import os

def resize(fname, fnew_name=None, large_img_size=None):
    large_size = large_img_size or (888, 888)

    im = Image.open(fname)

    image_w, image_h = im.size
    aspect_ratio = image_w / float(image_h)
    new_height = int(large_size[0] / aspect_ratio)

    if new_height < large_size[1]:
        final_width = large_size[0]
        final_height = new_height
    else:
        final_width = int(aspect_ratio * large_size[1])
        final_height = large_size[1]

    imaged = im.resize((final_width, final_height), Image.ANTIALIAS)

    #imaged.show()
    if not fnew_name:
        fnew_name = os.path.splitext(fname)[0] + '_888.jpg'
    imaged.save(fnew_name, quality=90)

if __name__ == '__main__':
    extensions = ('.JPG', '.jpg', '.jpeg', '.JPEG')
    for fname in (name for name in os.listdir()
                    if name.endswith(extensions)):
        resize(fname)
