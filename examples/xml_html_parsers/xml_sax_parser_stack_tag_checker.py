#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.sax


class Stack(object):
    """LIFO stack"""

    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def pop_or_none(self):
        if self.is_empty():
            return None
        return self.pop()

    def peek(self):
        return self._items[-1]

    def peek_or_none(self):
        if self.is_empty():
            return None
        return self.peek()

    def size(self):
        return len(self._items)

    def __str__(self):
        return '.'.join(self._items)


class CloseTagChecker(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self._stack = Stack()
        self._plugin_name = ''

    def startElement(self, name, attrs):
        self._stack.push(name)

    def characters(self, content):
        _current_element = self._stack.peek()
        if _current_element == 'name':
            self._plugin_name = content

    def endElement(self, name):
        el = self._stack.pop()
        if el != name:
            msg = 'Tag that must be close: {} Found end tag in XML: {}'.format(el,name)
            print(msg)

    def get_plugin_name(self):
        return self._plugin_name


if __name__ == "__main__":
    handler = PluginInfoHandler()
    xml_fname = 'test.xml'
    xml.sax.parse(xml_fname, handler)
    print(handler.get_plugin_name())