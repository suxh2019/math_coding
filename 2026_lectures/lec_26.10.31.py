# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:59:22 2026

@author: xihong
"""
# Permutations

'''
Given an array nums of unique integers, return all the 
possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [7]
Output: [[7]]
'''

'''
Intuition: 
  1.the idea is to generate permutations by 
building them from smaller permutations.

Algorithm: 
  1.If the list is empty → the only permutation is [].
  2. Otherwise:
        (1)Take the first number of the list.
        (2)Recursively get all permutations of the remaining 
        numbers. 
        (3) For each smaller permutation, insert the first number into every possible position.
           Example:
           If smaller permutation = [2,3] and new number = 1,
             we create: [1,2,3], [2,1,3], [2,3,1].
             This works because inserting the new number 
             in all positions ensures we build all unique 
             permutations.
'''

def permute(nums):
        res = []
        
        
        return res
print(permute([1,2,3]))