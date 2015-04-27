#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 07"""


# Import Python libs
import unittest
import os
import pickle


# Import user libs
from picklecache import PickleCache


class Task07TestCase(unittest.TestCase):
    """Task 07 tests"""

    def test_picklecache_autosync_set(self):
        """Tests that autosync triggers when adding/changing an item."""
        if os.path.exists('datastore.pkl'):
            os.unlink('datastore.pkl')

        data = ['Winkin', 'Blinkin', 'Nod']
        fpath = 'datastore.pkl'
        pcache = PickleCache(fpath, autosync=True)
        pcache['data'] = data

        fhandler = open(fpath, 'r')
        retrieved = pickle.load(fhandler)
        fhandler.close()

        self.assertEqual(retrieved, {'data': data})

    def test_picklecache_autosync_del(self):
        """Tests that autosync triggers when deleting an item."""
        if os.path.exists('datastore.pkl'):
            os.unlink('datastore.pkl')

        data = ['Winkin', 'Blinkin', 'Nod']
        fpath = 'datastore.pkl'
        pcache = PickleCache(fpath)
        pcache['data'] = data
        pcache.flush()

        pcache.autosync = True
        del pcache['data']

        fhandler = open(fpath, 'r')
        retrieved = pickle.load(fhandler)
        fhandler.close()

        self.assertEqual(retrieved, {})


if __name__ == '__main__':
    unittest.main()
