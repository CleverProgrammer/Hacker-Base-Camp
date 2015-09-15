# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:55:56 2015
2048_merge_attempt1.py
@author: Rafeh
"""
import unittest


def merge(nums):
    '''
    Takes a list as input
    returns merged pairs with
    non zero values shifted to the left.
    fancy interactive doc test below, no output means no problems.
    >>> merge([2, 0, 2, 4])
    [4, 4, 0, 0]
    >>> merge([0, 0, 2, 2])
    [4, 0, 0, 0]
    >>> merge([2, 2, 0, 0])
    [4, 0, 0, 0]
    >>> merge([2, 2, 2, 2, 2])
    [4, 4, 2, 0, 0]
    >>> merge([8, 16, 16, 8])
    [8, 32, 8, 0]
    '''
    pairs = []
    prev = None
    for num in nums:
        if not num:
            continue
        if prev is None:
            prev = num
        elif num == prev:
            pairs.append(num+prev)
            prev = None
        else:
            pairs.append(prev)
            prev = num
    if prev is not None:  # Append last value if non-zero
        pairs.append(prev)
    pairs.extend([0] * (len(nums) - len(pairs)))
    return pairs


class Test(unittest.TestCase):
        # python -m unittest 2048_merge_attempt1.py in Terminal
    def test1(self):
        # self.assertEqual(function(input), expected_output)
        self.assertEqual(merge([0, 0, 2, 2]), [4, 0, 0, 0])

    def test2(self):
        self.assertEqual(merge([2, 0, 2, 4]), [4, 4, 0, 0])

    def test3(self):
        self.assertEqual(merge([2, 2, 0, 0]), [4, 0, 0, 0])

    def test4(self):
        self.assertEqual(merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])

    def test5(self):
        self.assertEqual(merge([8, 16, 16, 8]), [8, 32, 8, 0])

    def test6(self):
        self.assertEqual(merge([8, 16, 16, 8, 2, 6]), [8, 32, 8, 2, 6, 0])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
