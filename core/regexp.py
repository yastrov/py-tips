#!/usr/bin/env python
#encoding: utf-8

__doc__ = """Regular expression examples, snippets.
"""

import re

def lower1(data):
    callback = lambda pat: pat.group(1).lower()
    r = re.sub(r'([A-Z]){2}', callback, data)
    return r

def lower2(data):
    callback = lambda pat: pat.group(1).lower()
    r = re.sub(r'([A-Z])\1', callback, data)
    return r

#--------
#Group
def toLowercase(matchobj):
   return matchobj.group(1).lower()

def lower3(data):
    r = re.sub(r'([A-Z]){2}', toLowercase, data)
    return r
#-------------

def tol(m):
   return m.group(0)[0].lower()

def lower4(data):
    r = re.sub(r'([A-Z]){2,}', tol, data)
    return r

if __name__ == '__main__':
    s = '24,105 and 56,95 euro'
    print(s)
    #Find
    #Search one element
    match = re.search(r'[\d\.,]+', s)
    if match is not None:
        print('found: {}'.format( match.group() ))
    else:
        print('did not find')
    #You can
    # obj = re.compile(r'[\d\.,]+')
    # match = obj.findall(s)
    match = re.findall(r'[\d\.,]+', s)
    for el in match:
        print(el)
    match = re.findall(r'([\d\.,]+)[.,]([\d\.,]+)', s)
    print(match)

    #Match
    w = "Ian Malcolm"
    match = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)",
                     w)
    print(match.groupdict())
    print(match.group('last_name'))

    match = re.match(r'([\d\.,]+)[.,]([\d\.,]+)', s)
    print(dir(match))
    print(match.groups())
    #Replace
    s2 = 'start TTT AAA end'
    print(lower1(s2))
    print(lower2(s2))
    print(lower3(s2))
    print(lower4(s2))
    ## re.sub(pat, replacement, str) -- returns new string with all replacements,
    ## \1 is group(1), \2 group(2) in the replacement
    #Replace ',' to '.'
    r = re.sub(r'([\d\.,]+),([\d\.,]+)', r'\1.\2', s)
    print(r)
