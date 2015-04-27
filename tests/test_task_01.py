#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01"""


# Import Python libs
import unittest
import os
import pickle


# Import user libs
from picklecache import PickleCache


class Task01TestCase(unittest.TestCase):
    """Task 01 tests """

    def test_picklecache_exists(self):
        """Check to see if the class exists"""
        self.assertTrue(PickleCache)

    def test_picklecache_file_path(self):
        """Tests the value of the file_path autosync"""
        cacher = PickleCache('banana.pkl')
        self.assertEqual(cacher._PickleCache__file_path, 'banana.pkl')

    def test_picklecache_autosync(self):
        """Tests the value of the autosync attribute"""
        cacher = PickleCache()
        self.assertFalse(cacher.autosync)
        cacher = PickleCache(autosync=True)
        self.assertTrue(cacher.autosync)

    def test_picklecache_file_path_default(self):
        """Tests the default value of the file_path parameter"""
        cacher = PickleCache()
        self.assertEqual(cacher._PickleCache__file_path, 'datastore.pkl')

    def test_picklecache_data(self):
        """Tests the default value of __data"""
        if os.path.exists('datastore.pkl'):
            os.unlink('datastore.pkl')

        cacher = PickleCache()
        self.assertEqual(cacher._PickleCache__data, {})


if __name__ == '__main__':
    unittest.main()
