#!/usr/bin/env python
# -*- coding: utf-8 -*-
from html.parser import HTMLParser


class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._img_urls = []

    def handle_starttag(self, tag, attrs):
        """Вызовется при открытии любого тега
        tag - имя, название тега
        attrs - список аттрибутов (параметров), в формате: (имя, значение)
        """
        if tag == 'img':
            # один вариант, не самый быстрый
            _url = dict(attrs).get('src', '')
            if _url.startswith('http'):
                self._img_urls.append(_url)

    def get_img_urls(self):
        return self._img_urls


class MainLinkParser(HTMLParser):
    """
    Казалось бы лучший вариант, одно но: может попастся испорченная HTML
    страничка, и тогда LinkParser упадёт с ошибкой.
    """
    def __init__(self):
        super().__init__()
        self._urls = []

    def handle_starttag(self, tag, attrs):
        """Вызовется при открытии любого тега
        tag - имя, название тега
        attrs - список аттрибутов (параметров), в формате: (имя, значение)
        """
        if tag == 'a':
            # Другой вариант, должен быть быстрее
            for name, value in attrs:
                if name == 'href':
                    if value.startswith('http://'):
                        self._urls.append(value)
                    break

    def get_urls(self):
        return self._img_urls


if __name__ == "__main__":
    data = """<html> ... """
    p = MainLinkParser()
    p.feed(data)
    urls = p.get_urls()
