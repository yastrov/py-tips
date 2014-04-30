#!/usr/bin/env python
"""
Myproj
============
 

"""

from setuptools import setup, find_packages
 
import myproj
 
setup(
    name="myproj",
    version=myproj.__version__,
    description="Description",
    long_description=__doc__,
    author=myproj.__author__,
    url="http://example.com/myproj",
    license=myproj.__license__,
 
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "License :: Freely Distributable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
 
    platforms='any',
    install_requires=[
        "requests>=1.0",
    ],
    #for small script:
    #py_modules=['myfile_library_single_file'],
    #scripts=['myfile_main'],
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            myproj = myproj.main:main'
        ],
        'gui_scripts': [
            'mygui = myproj.main:start_func',
        ]
    },
)
