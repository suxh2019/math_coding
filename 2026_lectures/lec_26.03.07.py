# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 08:40:09 2026

@author: xihong

Review Session
"""

print()
print("-------Question 1-------")
print()

# Given a list of numbers, write a for loop to count how many values that are 
# greater than -5 and less than 100, and the print the count number
numbers = [-4,6,10,66,-15,99,30,50,100,20, 30,-10,8]

#Write your code below




print()
print("-------Question 2-------")
print()
# Given a list of grades, write code to compute the average grade
# In this case, the average grade is  84. 
grades = [80,70,75,95,100,50,30]

#Write your code below




print()
print("-------Question 3-------")
print()

# write a function to compute num1 * num2 + num3 and return the result
def mul_add(num1,num2,num3):
    
    
    
    
    
    return 0

#------------keep the test code unchanged------------
a = 5
b = 16
c =10
res = mul_add(a, b,c)
print(a,"*", b , "+",c,"=", res)
#------------keep the test code unchanged------------




print()
print("-------Question 4-------")
print()
# Given a list of numbers, assume that these numbers are increased by 10 or decresed by 10
# for example, the list can [10,20,30], or [40,30,20,10,0], or [100,110,120,130] and so on
# Given such a special list, write a function to find the THIRD highest value 
# in the list, return the second highest value

def find_third_highest_value(list):
    
    
    
    
    
    
    return 0

#------------keep the test code unchanged------------
list_one = [10, 20, 30,40,50]
second_highest_value =  find_third_highest_value(list_one)
print("The second highest value in the first list is ", second_highest_value )
list_two = [120, 110, 100,90,80,70,60,50]
second_highest_value =  find_third_highest_value(list_two)
print("The second highest value in the second list is ", second_highest_value )
#------------keep the test code unchanged------------




print()
print("-------Question 5-------")
print()
'''
 The len() function in Python is a built-in function that returns the
 number of items in an object. It works with various data types, including 
 strings, lists, tuples, dictionaries, sets, and range objects
'''

# Given a list of positve numbers, return the index of the maximum value
# in the list. Add one line code below to save the index of the maximum value


mylist = [10,15,3,1,0,20,16]
n = len(mylist)
max_value = -1
index = 0

for i in range(0,n):
    if mylist[i] > max_value:
        max_value = mylist[i]
        
        
        
 # The maximum value is 20  
print("The maximum value is the list is ", max_value)
# The correct index is 5
print("The index of the maximum value is  ", index) 





print()
print("-------Question 6-------")
print()


# Given a list of positve numbers, swap the first value  with
# the maximum value is the list

mylist = [10,15,3,1,0,20,16]
n = len(mylist)
max_value = -1
index = 0

for i in range(0,n):
    if mylist[i] > max_value:
        max_value = mylist[i]
        
        
# write the code below to swap the first value with the maximum value



# The original list is   [10, 15, 3, 1, 0, 20, 16]  
print("The original list is  ", mylist) 

# The new list is  [20, 15, 3, 1, 0, 10, 16]
print("The new list is  ", mylist)



print()
print("-------Question 7-------")
print()

# Given a Sorted list in ascending order. Write the code to PRINT the 
# first 5 smallest nunmbers 


def five_little_numbers(mylist):
    # hint: use for loop and range 
    
    
    
   # keep the return below unchanged
   return


test_list = [1,3,4,5,6,7,8,9,10,24,35,44,55,66,77,88,99]
print(" The five little numbers are ")
# The correct output includes 1,3,4,5,6. 
five_little_numbers(test_list)

print()
print("-------Question 8-------")
print()

# Given a Sorted list in ascending order. Write the code to PRINT the 
# first 5 largest nunmbers in any order

def five_large_numbers(mylist):
    # hint: use for loop and range, read numbers for the end of the list
    
    
    
   # keep the return below unchanged
   return


test_list = [1,3,4,5,6,7,8,9,10,24,35,44,55,66,77,88,99]
print(" The five large numbers are ")
# The correct output includes 99,88,77,66,55 
five_large_numbers(test_list)




