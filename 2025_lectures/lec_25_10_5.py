# -*- coding: utf-8 -*-
"""
Created on Sun Octomber 5, 2025

@author: xihong
"""



# How to read and save each element from a list

list_nums = [1,7,8]


for element in list_nums:
    a = element # save the element value to the variable a 
    print("Now the value a is ", a)



'''
Write a function to find the minimum value of a list
function name: find_min
parameter: list

'''

def find_min(list):
    
    smallest_value = 1000000
    
    for element in list:
        if element < smallest_value:
            smallest_value = element
    return smallest_value


# Call the function

list = [1,4,0,11,40,57,100,-100,-1000,3000]
small_value = find_min(list)

print("The smallest value of the list is : ", small_value)


