#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 06"""


# Import Python libs
import unittest
import os
import pickle


# Import user libs
from picklecache import PickleCache


class Task06TestCase(unittest.TestCase):
    """Task 06 tests"""

    def test_picklecache_flush_data(self):
        """Tests that flush saves data to the file object."""
        if os.path.exists('datastore.pkl'):
            os.unlink('datastore.pkl')

        data = ['Winkin', 'Blinkin', 'Nod']
        fpath = 'datastore.pkl'
        pcache = PickleCache(fpath)
        pcache['data'] = data
        pcache.flush()

        fhandler = open(fpath, 'r')
        retrieved = pickle.load(fhandler)
        fhandler.close()

        self.assertEqual(retrieved, {'data': data})


if __name__ == '__main__':
    unittest.main()
