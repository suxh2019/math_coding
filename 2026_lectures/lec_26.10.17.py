# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:53:40 2026

@author: xihong
"""
print("----Basic Operations-----")
# Use append() to add an element to the end of a list
mylist = [1, 2, 3, 11, 20, 2, 4, 7]
mylist.append(10)
print(" The new list after adding 10 is: ", mylist)

# Use remove() to delete by value:.
mylist.remove(2)
print(" The new list after removing 2 is: ", mylist)

# Use pop() to delete the last element.
mylist.pop()
print(" The new list after the pop operation is: ", mylist)

# Use pop(i) to delete the element at the index i:
i = 0
mylist.pop(i)
print(" The new list after popping the  ", i, "th element is ", mylist)
print()

# Question 1:
'''
Given an integer array numbers and an integer target,
 remove all occurrences of target in numbers. The order 
 of the elements may be changed. Then return the number 
 of elements in nums which are not equal to target.
 
 Example 1:
     Input: numbers = [3,2,2,2,3], target = 3
     Output: 2, numbers = [2,2,2]
'''

def removeElement(numbers, target):
    count = 0
    result = [] 
   
    
    
     
    return count, result
 
# Test cases
print("---The first test case---")
nums1 = [4,4,5,3,4]
target = 4
count, result = removeElement(nums1, 4)
print("The occurence of ", target, " is ", count )
print("The new array of numbers is ", result)
print()
print("---The second test case---")
nums2 = [1,5,3,4]
target2 = 0
count2, result2 = removeElement(nums2, 0)
print("The occurence of ", target2, " is ", count2 )
print("The new array of numbers is ", result2)
print()

'''
A character is a single symbol, such as:'a'
'B','7','!',' '

A string is a sequence of characters. 
In Python, strings are written inside quotes:
name = "hello"
''' 

# Question 2: Reverse String
'''
You are given an array of characters which
 represents a string s. Write a function 
 which reverses a string.
Example 1:

Input: s = ["n","e","e","t"]

Output: ["t","e","e","n"]
Example 2:

Input: s = ["r","a","c","e","c","a","r"]

Output: ["r","a","c","e","c","a","r"]

'''  
def reverseString(s):
    output = []
    
    
    return output
print()
print("----test cases---")
print(reverseString(["n","e","e","t"]))
print(reverseString(["r","a","c","e","c","a","r"]))