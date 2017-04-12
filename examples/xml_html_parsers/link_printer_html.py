#!/usr/bin/env python
# -*- coding: utf-8 -*-
from html.parser import HTMLParser

class LinkPrinter(HTMLParser):
    """
    Preant each link from HTML web page
    """
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    print(value)

# data = ...
LinkPrinter().feed(data)
