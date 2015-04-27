#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 04"""


# Import Python libs
import unittest
import os
import pickle


# Import user libs
from picklecache import PickleCache


class Task04TestCase(unittest.TestCase):
    """Task 04 tests"""

    def test_picklecache_delete(self):
        """Tests the delete functionality of PickleCache."""
        pcache = PickleCache()
        pcache['foo'] = 'bar'
        self.assertEqual(pcache['foo'], 'bar')
        del pcache['foo']

        with self.assertRaises(KeyError):
            pcache['foo']

if __name__ == '__main__':
    unittest.main()
