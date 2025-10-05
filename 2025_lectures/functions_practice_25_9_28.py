# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 14:26:49 2025
Edited on 10/5/2025

@author: xihong
"""


'''
The syntax for if-else

if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
the condition in the if statement is True, the block of code under if is executed;
 otherwise, the block under else is executed.

'''
print("-------------------------")
a = 4
b =7

if a > b :
    print("a is bigger")
else:
    print("b is bigger")
    
print("---------------")   
# return the bigger number from two different numbers
# print which number is bigger
def return_bigger_number(num1,num2):
    
    bigger_number = 0
    
    if num1 > num2 :
       
        bigger_number = num1
        
    else:
        bigger_number = num2
        
    return bigger_number


num1 = 100
num2 = 10

bigger_value = return_bigger_number(num1,num2)
#print("The bigger value between", num1,"and", num2,"is",bigger_value)



'''
write a function to compare three different numbers
and return the biggest number
function name: compare_three_numbers
hint: use if-else statement
'''
def compare_three_numbers(num1,num2,num3):
    
    # save the biggest value among three numbers
    biggest_value = 0
    # save the bigger value among two numbers
    bigger_value = 0
    
    if num1 > num2:
        bigger_value = num1
    else:
        bigger_value = num2
        
    if bigger_value > num3:
        biggest_value =bigger_value
    else:
        biggest_value = num3
    
    return biggest_value


num1 = 10
num2 = 50
num3 = 5

big_value = compare_three_numbers(num1,num2,num3)
print("The biggest value is ", big_value)

print()
print()


# Use the for loop to find the maximum value from the list
def compare_list(list):
    
    # save the biggest value among three numbers
    biggest_value = -1000
    
    for element in list:
        if element > biggest_value:
            biggest_value = element
    
    return biggest_value

list =[1,7,3,18,37,11,41,67]
value = compare_list(list)
print("biggest value is: ",value)












