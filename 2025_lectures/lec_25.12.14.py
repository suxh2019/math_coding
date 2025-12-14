# -*- coding: utf-8 -*-
"""
Created on Sun 12/14



@author: xihong
"""

print()
print("---------------")
# code to swap two variables

x = 5
y = 10

print('The value of x before swapping', x)
print('The value of y before swapping', y)


print()
print("---------------")
x = 5
y = 10
# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping', x)
print('The value of y after swapping', y)


print()
print("---------------")

list_before_swap = [10,5,2,11,70]
print("The original list is : ", list_before_swap)
print()

#Print the first element
print("The first element in list_before_swap ia: ",list_before_swap[0])

#Print the third element
print("The third element in list_before_swap ia: ",list_before_swap[2])
print()

'''
Swap two elements in a list 
Use a temporary variable to store one element while swapping
'''
temp = list_before_swap[0]
list_before_swap[0] = list_before_swap[2]
list_before_swap[2]= temp

print("The list after swapping the first element and the third element is : ", list_before_swap)

print()
print("------------sorting numbers--------------------------")

# Sort a list of numbers in ascending order
'''
1. Bubble sort: 
    (1) adjacent elements are compared and swapped if they are in the wrong order, 
    (2) repeat the process (1) until no more swaps are needed
2. Implementation:
    (1) two nested loops
    (2) the outer loop controls the number of passes 
    (3) the inner loop performs the comparisons and swaps
'''


# Example explanation: five students stand in a line.
# Jennifer: hold number num1
# Seraphina: hold number num2
# Xinwen: hold number num3
# Joseph: hold number num4
# Claire:  hold number num5

# 1) Start with the first person, Jennifer, in the line, compare  num1 Jennifer holds
#     with num2 her neighbor, Seraphina, holds, 
#        if num1 > num2, swap Jennifer and Seraphina

# 2) compare the number the second person holds with the number the third person holds
#              if the number the second person holds > the number the third person holds
#                     swap the second person and the third person\
    
# 3) repeat the above process, and compare the number the second-to-last person holds
#                   with the number the last person holds

# 4) Repeat step 1) - 3) five times (the number of students)



'''
1. Selection sort: 
    (1) Find the minimum element from the unsorted portion of the list and swapping 
        it with the first unsorted element.
2. Implementation:
    (1) two nested loops
    (2) the outer loop runs from the first element to the second-to-last element
    (3) the inner loop finds the smallest element in the remaining unsorted segment, 
        and swaps it with the first unsorted element
'''

# Example explanation: five students stand in a line.
# Jennifer: hold number num1
# Seraphina: hold number num2
# Xinwen: hold number num3
# Joseph: hold number num4
# Claire:  hold number num5


# 1) find the smallest value from [num1, num2,num3,num4,num5], swap the person who
#    holds the smallest value with the person who stands in the first place in the line

# 2) find the second smallest value, swap the person who holds the second
#   smallest value with the person who stands in the second place in the line

# 3) find the third smallest value, swap the person who holds the third smallest
# value with the person who stands in the third place in the line

# and so on.