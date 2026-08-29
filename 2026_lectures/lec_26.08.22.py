# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:43:31 2026

@author: xihong
"""
print()
print("---Project 1----")
print()
# Project 1: Palindrome
'''
Given a string s, return true if it is a palindrome,
 otherwise return false.

A palindrome is a string that reads the same forward 
and backward. It is also case-insensitive and ignores 
all non-alphanumeric characters.

Examples:
    1. input: s = "abba", output: True
    2. input: s = "aba",  output: True
    3. input: s = "abab", output: False  
'''
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) -1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right -1
    return True

# Test cases
print(isPalindrome("abba"))
print(isPalindrome("aba"))
print(isPalindrome("abab"))
print(isPalindrome("aaaaaaaaaaaa"))
print(isPalindrome("aaaaabababaaaaa"))

print()
print("---Project 2----")
print()
# Project 2: Contains dupilciate
'''
Given an integer array nums, return true if any 
value appears more than once in the array, 
otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]
Output: true

Example 2:

Input: nums = [1, 2, 3, 4]
Output: false
'''   
def hasDuplicate(nums): 
    
    
     return False
    
# Test cases
print(hasDuplicate([1, 2, 3, 3]))
print(hasDuplicate([1, 2, 3, 4]))
print(hasDuplicate([1, 2, 3, 4, 5, 6,7]))
print(hasDuplicate([1, 1, 2, 3, 4, 5, 6,7]))

print()
print("---Project 3----")
print()
# Project 3: Two Sum
'''
Given an array of integers nums and an integer target,
 return the indices i and j such that 
nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair
of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10

Output: [0,2]
'''
def twoSum(nums, target):
    
    return [0,1]


# Test cases:
print(twoSum([3,4,5,6], 7))
print(twoSum([4,5,6], 10))
print(twoSum([4,5,6,8,9,20], 15))
    
    
    


   