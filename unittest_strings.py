#!/usr/bin/env python3
#
# https://docs.python.org/3/library/unittest.html

import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_list(self):
        L = [1, 2, 3]
        self.assertListEqual(L, [1, 2, 3])

    def test_dict(self):
        D = {'a': 1, 'b': 2, 'c': 3}
        self.assertDictEqual(D, {'a': 1, 'b': 2, 'c': 3})


if __name__ == '__main__':
    unittest.main()
