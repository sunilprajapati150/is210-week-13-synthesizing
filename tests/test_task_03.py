#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 03"""


# Import Python libs
import unittest
import os
import pickle


# Import user libs
from picklecache import PickleCache


class Task03TestCase(unittest.TestCase):
    """Task 03 tests """

    def test_picklecache_get(self):
        """Gets a value from picklecache."""

        legos = ['brick', 'axel', 'wheel', 'wing', 'figure']

        pcache = PickleCache()
        pcache['apple'] = 'jack'
        pcache['legos'] = legos

        self.assertEqual(pcache['apple'], 'jack')
        self.assertIs(pcache['legos'], legos)

    def test_picklecache_get_missing(self):
        """Confirm that it throws a KeyError when a key is missing."""
        pcache = PickleCache()
        with self.assertRaises(KeyError):
            pcache['apple']


if __name__ == '__main__':
    unittest.main()
