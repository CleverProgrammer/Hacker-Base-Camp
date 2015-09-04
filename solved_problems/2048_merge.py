# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:55:56 2015
2048_merge_attempt1.py
@author: Rafeh
"""
import unittest
import doctest


def merge(nums):
    '''
    Takes a list as input
    returns merged pairs with
    non zero values shifted to the left.
    fancy interactive unit test below, no output means no problems.
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
    slide = []  # Append non-zeroes first
    for num in nums:
        if num != 0:
            slide.append(num)
    for num in nums:
        if num == 0:
            slide.append(num)
    pairs = []
    for idx, num in enumerate(slide):
        if idx == len(slide)-1:
            pairs.append(num)
            if len(pairs) != len(nums):
                pairs.append(0)
            break
        if num == slide[idx+1]:
            if num != 0:
                pairs.append(num*2)
                slide[idx+1] -= slide[idx+1]
                # slide[idx+1], slide[idx+2] = slide[idx+2], slide[idx+1]
            else:
                pairs.append(num)
        else:
                pairs.append(num)  # Even if they don't match you must append
    slide = []  # Append non-zeroes first
    for num in pairs:
        if num != 0:
            slide.append(num)
    for num in nums:
        if num == 0:
            slide.append(num)
    for i in range(len(nums) - len(slide)):
        if len(nums) != len(slide):
            slide.append(0)
    return slide

doctest.testmod()


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
