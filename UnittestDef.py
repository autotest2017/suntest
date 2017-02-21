#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest


class TestStringMethods1(unittest.TestCase):
    def setUp(self):
        self.name = 'XH'
        print ('setup is called')

    def tearDown(self):
        del self.name
        print ('teardown is called')

    @classmethod
    def setUpClass(cls):
        print ('from setupclass')

    @classmethod
    def tearDownClass(cls):
        print ('from teardownclass')

    def test_upper(self):
        print (self.name)
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print (self.name)
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


class TestStringMethods2(unittest.TestCase):
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        # with self.assertRaises(TypeError):
        #     s.split(2)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestStringMethods1))
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not res.wasSuccessful())

    # from setupclass
    # setup is called
    # XH
    # teardown is called
    # setup is called
    # XH
    # teardown is called
    # from teardownclass