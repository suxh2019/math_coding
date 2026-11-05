# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:18:39 2026

@author: xihong
"""

'''
Meeting room:
    
Given an array of meeting time interval 
objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
determine if a person could add all meetings to their 
schedule without any conflicts. The intervals may be 
provided in any order.

Note: (0,8),(8,10) is not considered a conflict at 8
'''

# Examples:
'''
Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true

'''

# intervals.sort(key = lambda intervals:intervals[0])
'''
intervals.sort(key = lambda intervals:intervals[0])
Explaination: sorts a list of intervals in ascending order based on the 
first element of each interval

.sort() is a built-in Python list method.It sorts the 
elements of a list in place, meaning it modifies the 
original list.

key=
The key parameter tells Python which value to use when 
sorting each element

lambda intervals: intervals[0]
A lambda expression defines a small anonymous function.
Its general syntax is: lambda arguments: expression

lambda intervals: intervals[0]

- lambda: Creates an anonymous function.
- intervals: The input argument, representing one interval.
- intervals[0]: Returns the first element of that interval.
'''
def canAttendMeetings(intervals):
    # sorts a list of intervals in ascending order based 
    # on the first element of each interval.
    intervals.sort(key = lambda intervals:intervals[0])
    
    
  
    return True

# Test case
print("---test case 1---")
intervals = [(0,30),(5,10),(15,20)]
print("Test case 1: ", canAttendMeetings(intervals))

print("---test case 2---")
intervals = [(5,8),(9,15)]
print("Test case 2: ", canAttendMeetings(intervals))






