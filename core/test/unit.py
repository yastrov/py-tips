#!/usr/bin/env python
#encoding: utf-8

__doc__ = """Unittest examples, snippets.

Use:
python3 unit.py -v
"""
import unittest
from d1 import summ

class TestSumm(unittest.TestCase):

    def testSummInt(self):
        s = summ(1, 2)
        self.assertEqual(s, 3)


if __name__ == '__main__':
    unittest.main()