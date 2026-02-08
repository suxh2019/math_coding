# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 15:45:16 2026

@author: xihong
"""

# Swap two variables using temporary variable

'''
1)  Store the value of the first variable (x) in a temporary variable(temp). 
2) Assign the value of the second variable(y) to the first variable(x). 
3 Assign the value stored in the temporary variable(temp) to the second variable(y). 

'''

# x = 10
# y = 20

# print("The value of x is ", x)
# print("The value of y is ", y)

# print("-----after swapping----")
# # temp is the temporary variable
# temp = x
# x = y
# y = temp
# print("The value of x is ", x)
# print("The value of y is ", y)

# print()
# print("---------swap two varaibles without temporary variables")

# # Swap two variables without temporary variable
# '''
# Tuple Unpacking.No need to understand the concept now. 
# Remember the result, for example, x,y = y,x 
# '''

# x = 10
# y = 20

# print("The value of x is ", x)
# print("The value of y is ", y)

# print("-----after swapping----")

# x, y = y, x

# print("Now, the value of x is ", x)
# print("Now, the value of y is ", y)



print()
print("-----bubble sort----")

def bubble_sort(arr):
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

mylist = [5,4,1,3]
sorted_list = bubble_sort(mylist)
print("The sorted list is ", sorted_list)

'''
n = len(arr), then n = 4

i = 0 
    j = 0, compare arr[0] with arr[1], 5 > 4, swap arr[0] and arr[1]
       arr = [4,5,1,3]
    j = 1, compare arr[1] with arr[2], 5 > 1, swap arr[1] and arr[2]
       arr = [4,1,5,3]
    j = 2, compare arr[2] with arr[3], 5> 3, swap arr[2] and arr[3]
       arr = [4,1,3,5]
    
i = 1
   j = 0, compare arr[0] with arr[1], 4 > 1, swap arr[0] and arr[1]
           arr = [1,4,3,5]
   j = 1, compare arr[1] with arr[2], 4 > 3, swap arr[1] and arr[2]
           arr = [1,3,4,5]
   j = 2, compare arr[2] with arr[3], 4> 5??, False, no swap
           arr = [1,3,4,5]
           
i = 2
   j = 0, compare arr[0] with arr[1], 1 > 3 ?? False, no swap
          arr = [1,3,4,5]
   j = 1, compare arr[1] with arr[2],3 > 4 ??, False, no swap
           arr = [1,3,4,5]
   j = 2, compare arr[2] with arr[3], 4> 5??, False, no swap
           arr = [1,3,4,5]
          
i = 3
   j = 0, compare arr[0] with arr[1], 1 > 3 ?? False, no swap
          arr = [1,3,4,5]
   j = 1, compare arr[1] with arr[2],3 > 4 ??, False, no swap
          arr = [1,3,4,5]
   j = 2, compare arr[2] with arr[3], 4> 5??, False, no swap
           arr = [1,3,4,5]

'''


# Below is the student's code.
# We will explain the variant version of selction sort 
# during the next class(2/28/26)

def sort_2(arr):
    # arr is  [5,4,1,3]
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
              
    return arr
mylist =  [5,4,1,3]
sorted_numbers = sort_2(mylist)
print("Selection sort result: ", sorted_numbers)

'''
n = 4

i = 0
   j =1, compare arr[0] with arr[1], 5 > 4, swap arr[0] and arr[1]
         arr = [4,5,1,3]
   j =2, compare arr[0] with arr[2], 4 > 1, swap arr[0] and arr[2]
         arr = [1,5,4,3]
   j =3, compare arr[0] with arr[3], 1 > 3?? False, no swap
         arr = [1,5,4,3]

i = 1
   j = 2, compare arr[1] with arr[2], 5 > 4, swap arr[1] and arr[1]
         arr = [1,4,5,3]
   j = 3, compare arr[1] with arr[3], 4 > 3, swap arr[1] and arr[3]
         arr = [1,3,5,4]
   
i = 2
   j = 3, compare arr[2] with arr[3], 5> 4,swap arr[2] and arr[3]
         arr = [1,3,4,5]
         
i = 3
   for j in range(i+1, n):
       
  that is range(4,4), so the code block will not be executed

'''


