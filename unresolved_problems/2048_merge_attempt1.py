# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:55:56 2015
2048_merge.py
@author: Rafeh
"""
nums = [2, 0, 2, 4]

# Append non-zeroes first
slide = []
for num in nums:
    if num != 0:
        slide.append(num)

# Append zeroes last
for num in nums:
    if num == 0:
        slide.append(num)
        
pairs = []
for idx, num in enumerate(slide):
    if idx == len(slide)-1:
        break
    pair = slide[idx] == slide[idx+1]
    if pair:
        if idx == 0:
            pairs.append(slide[idx]*2)
            pairs.append(0)
        elif slide[idx] != slide[idx-1]:
            pairs.append(slide[idx]*2)
            pairs.append(0)

print(" Nums: %s" %nums)
print("Slide: %s" %slide)
print("Pairs: %s" %pairs)
        