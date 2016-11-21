#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""synthesizing task 13"""

import os
import pickle

class PickleCache(object):
    """
        picklecache class created

    """
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """ Class Constructor. takes two parameters

        Args:
            file_path(string, optional): defaults to 'datastore.pkl'
           
        Returns:
            
        Examples:
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__file_object
            None
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """stores key value pairs"""
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """ takes no arguments and returns lenght"""
        return len(self.__data)

    def __getitem__(self, key):
        """retrives data and handles if no data found"""
        try:
            return self.__data[key]
        except:
            raise KeyError('Parameter not found')

    def __delitem__(self, key):
        """removes unwanted objects """
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """takes the data and saves to a file"""
        if os.path.exists(self.__file_path) is True\
           and os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """saves the stored data for future use"""
        
        with open(self.__file_path, 'w') as fileget:
            pickle.dump(self.__data, fileget)
