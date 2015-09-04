# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:55:56 2015
2048_merge_attempt2.py
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
    if slide[idx] == slide[idx+1]:
        pairs.append(slide[idx] * 2)
        idx = idx + 1
    else:
        pairs.append(slide[idx])
        
    if slide[idx] == slide[idx+1]:  
        if idx == 0:
            pairs.append(slide[idx]*2)
        elif slide[idx] != slide[idx-1]: # Check if it's been already paired
            pairs.append(slide[idx]*2)

print(" Nums: %s" %nums)
print("Slide: %s" %slide)
print("Pairs: %s" %pairs)
        