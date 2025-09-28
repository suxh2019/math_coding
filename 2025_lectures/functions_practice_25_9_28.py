# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 14:26:49 2025


@author: xihong
"""

#---------part 1---------------------
'''
The syntax for if-else

if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
the condition in the if statement is True, the block of code under if is executed;
 otherwise, the block under else is executed.

'''

a = 4
b =7

if a > b :
    print("a is bigger")
else:
    print("b is bigger")
    
    
# return the bigger number from two different numbers
# print which number is bigger
def return_bigger_number(num1,num2):
    
    bigger_number = 0
    
    if num1 > num2 :
        print("num1 is bigger")
        bigger_number = num1
        
    else:
        print("num2 is bigger")
        bigger_number = num2
        
    return bigger_number


num1 = 100
num2 = 10

bigger_value = return_bigger_number(num1,num2)
print("The bigger value between", num1,"and", num2,"is",bigger_value)



'''
write a function to compare three different numbers
and return the biggest number
function name: compare_three_numbers
hint: use if-else statement
'''
def compare_three_numbers(num1,num2,num3):
    
    biggest_value = 0
    
    

    
    return biggest_value


'''
#---------------part 2---------------

# How to read and save each element from a list

list_nums = [1,3,6,7,8]

for element in list_nums:
    print(element) # print each element in the list
    
    a = element # save the element value to the variable a 
    print("Now the value a is ", a)
'''



#---------------------Part 3---------------------------

'''
Write a function to perform  power operation
result = base ** exponent
function name: power

'''






'''
Write a function to find the minimum value of a list
function name: find_min

'''




'''
Write the code to find the maximum value of a list
function name: find_max
''' 




x = -10
base = 2
exponent =3
list_num = [1,2,3,4,5,6,7]

'''
power_value = power(base, exponent)
min_value = find_min(list)
max_value = find_max(list)


print(base,"to the power ", exponent, "is", power_value)
print("The minimal value in ",list_num,"is", min_value)
print("The maximal value in ",list_num,"is", max_value)

'''

