#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.sax
from enum import Enum

# XML parser States
class Mode(Enum):
    init = 1
    tag_opened = 2
    tag_closed = 3


class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.__mode = Mode.init
        self.__content_buffer = []

    def startDocument(self):
        pass

    def endDocument(self):
        pass

    def startElement(self, name, attrs):
        self.__mode = Mode.tag_opened
        if name == "Item":
            for (k, v) in attrs.items():
                print(k, v)
            # Or as dict.
            dattrs = dict(attrs.items())
            num = dattrs.get('number', 1)
            print(num)

    def endElement(self, name):
        self.__mode = Mode.tag_closed
        content = ''.join(self.__content_buffer)
        self.__content_buffer.clear()

    def characters(self, content):
        if self.__mode is Mode.tag_opened:
            # content is chunk from full tag content.
            self.__content_buffer.append(content)

# Var 1
parser = xml.sax.make_parser()
parser.setContentHandler(MyHandler())
with open("test.xml","r") as fd:
    parser.parse(fd)

# Var 2
xml.sax.parse("test.xml", MyHandler())

# Var 3
handler = MyHandler()
with open("test.xml","r") as fd:
    xml.sax.parseString(fd.read().encode("utf-8"), handler)
