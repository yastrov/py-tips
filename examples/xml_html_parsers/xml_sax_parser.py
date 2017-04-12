#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        if name == "Item":
            for (k, v) in attrs.items():
                print(k, v)

# Var 1
parser = xml.sax.make_parser()
parser.setContentHandler(MyHandler())
with open("test.xml","r") as fd:
    parser.parse(fd)

# Var 2
handler = MyHandler()
with open("test.xml","r") as fd:
    xml.sax.parseString(fd.read().encode("utf-8"), handler)
