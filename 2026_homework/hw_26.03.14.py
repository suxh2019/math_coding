# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:23:54 2026

@author: xihong

"""

#Question 1:
'''
Review 2026_lectures\lec_26.02.07.py, use your English Words to describe the process of 
 
basic_bubble_sort function(mylist)  step by step, similar to the 
explaination in the  lec_26.02.07.py 

mylist = [9,4,1,3,2,0] 

'''

print()
print("----Basic -------bubble sort ------")
def basic_bubble_sort(arr):
    # arr is [5,4,1,3]
    n = len(arr)
    
    # i is the number Ms. Su holds
    for i in range(0,n):
        
        # j represents an index/position of each kid in the line
        for j in range(0, n-1):
            
            # Compare the value arr[j] the kid(stand in position j) 
            # holds with the value arr[j + 1] 
            # her/his neighbor(stand in position (j+1)) holds
            if arr[j] > arr[j + 1]:
                
                # Swap two values
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

mylist = [9,4,1,3,2,0]
sorted_list = basic_bubble_sort(mylist)
print("The sorted list is ", sorted_list)












