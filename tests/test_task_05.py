#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 05"""


# Import Python libs
import unittest
import os
import pickle


# Import user libs
from picklecache import PickleCache


class Task05TestCase(unittest.TestCase):
    """Task 05 tests"""

    def test_picklecache_load_constructor(self):
        """Tests that PickleCache load method loads the pickled data."""
        if os.path.exists('datastore.pkl'):
            os.unlink('datastore.pkl')

        fhandler = open('datastore.pkl', 'w')
        pickle.dump({'toads': ['Rash', 'Zitz', 'Pimple']}, fhandler)
        fhandler.close()

        pcache = PickleCache()
        self.assertEqual(pcache['toads'], ['Rash', 'Zitz', 'Pimple'])

    def test_picklecache_discrete_load(self):
        """Tests that picklecache can load data on discrete calls"""
        if os.path.exists('datastore.pkl'):
            os.unlink('datastore.pkl')

        pcache = PickleCache()
        self.assertEqual(len(pcache), 0)

        fhandler = open('datastore.pkl', 'w')
        pickle.dump({'apples': 'oranges'}, fhandler)
        fhandler.close()

        pcache.load()

        self.assertEqual(pcache['apples'], 'oranges')



if __name__ == '__main__':
    unittest.main()
