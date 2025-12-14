# -*- coding: utf-8 -*-
"""
Created on Sun 11/30

1) while loop; 2) if-elif-else

@author: xihong
"""

import random

# The syntax of while loop
'''
1) while keyword, 
2) a boolean expression (condition)
3) a colon
4) an indented block of statements that form the loop body

The general structure:
    
    while condition:
    statement(s)
    

How the while loop works:
1) Evaluate the condition at the beginning of each iteration
2) If the condition is True, the body of the loop is executed
3) After the body completes, the condition is checked again
4) The process repeats until the condition becomes False
       
'''
print("-----------")
count = 1
while count <= 3:
    print("Count is ", count)
    count += 1   


print()
print("--------------")
# print number 3,5,7,9,11

i = 1
while i < 10:
    i = i + 2
    print(i)
    
    
    
print()
print("---------------")
iterations = 0 
while True:
    number = random.randint(1, 100)
    iterations = iterations + 1
    if number <2:
       print("The number of iterations is ",iterations)
       break   
   
# Differences between for loop and while loop

'''
for loop:
    1) when the number of iterations is known 
    2) when iterating over a sequence of items, such as a lis
    
while loop:
    1) when the number of iterations is not known in advance 
    2) depends on a condition that may change during execution
'''

print()
print("---------------")
# if-elif-else statement
age = 12
if 0< age < 1:
    print('Baby')
elif 1<= age < 3:
    print('Toddler')
elif 3<= age < 5:
    print('Preschool')
elif 5<= age < 12:
    print('Gradeschooler')
elif 12<= age < 18:
    print('Teen')
elif 18<= age < 21:
    print('Young Adult')
else:
    print('Adult')


print()
print("---------------")
# code to swap two variables

x = 5
y = 10

print('The value of x before swapping', x)
print('The value of y before swapping', y)

print()
print("---------------")
# try
x = y
y = x

print('The value of x is:  ', x)
print('The value of y is : ', y)

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

# How to sort a list of numbers in ascending order
