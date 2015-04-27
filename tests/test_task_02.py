#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 02"""


# Import Python libs
import unittest
import os
import pickle


# Import user libs
from picklecache import PickleCache


class Task02TestCase(unittest.TestCase):
    """Task 02 tests """

    def test_picklecache_set(self):
        cacher = PickleCache()
        cacher['apple'] = 'jack'
        self.assertEqual(cacher._PickleCache__data['apple'], 'jack')

    def test_picklecache_len(self):
        cacher = PickleCache()
        cacher['apple'] = 'jack'
        cacher['legos'] = ['brick', 'axel', 'wheel', 'wing', 'figure']
        self.assertEqual(len(cacher), 2)


if __name__ == '__main__':
    unittest.main()
