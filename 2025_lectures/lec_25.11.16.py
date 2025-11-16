# -*- coding: utf-8 -*-
"""
Created on Sun 11/16

1) summarize the common mistakes in two exams
2) while loop
3) project

@author: xihong
"""


'''
Common mistakes in the two exams

'''

# 1. = and ==
'''
 1) The = operator is the assignment operator, used to assign a value to a variable.
  for example, let a = 3; assigns the value 3 to the variable a
 2) The == operator is the equality operator, which compares whether the values of 
two operands are equal. It returns True if the values are the same and False otherwise
  
  '''
print()
print("-----1---=-and == ----")
print()

a = 3
b = 4
c = 3

print("The value of a is : ", a)
print("The value of b is : ", b)
print("The value of c is : ", c)

print()

print("Result of a == b: ", a == b)
print("Result of a == c: ", a == c)

print()
a = b
print("The value of a is now: ", a)


# 2. return
'''
The "caller" refers to the function or code block that initiates a call to another function
The "callee" is the function that is being called.


1)  The return keyword is used to exit a function and send a value back to the caller
2) When a return statement is executed, the function's execution terminates immediately
3) A function can contain multiple return statements, but only the first one encountered during execution will be executed
  
  '''
print()
print("-----2 -- return----keyword----")
print()


def add(num1,num2):
    result = num1 + num2
    return result

a = 5
b = 100
sum_two_numbers = add(a,b)
print( a, "+",b,"=",sum_two_numbers)


print()
def for_loop(list, target):
    
    for value in list:
        if value == target:
            #break # break exit only from the for loop
            return "found"
    return "Not found"

mylist = [1,2,3,4,5,6,7]
result = for_loop(mylist, 9)
print("found? ", result)
result_1 = for_loop(mylist, 2)
print("found? ", result_1)



print()
def substraction(num1,num2):
    result = num1 - num2
    
    return 0
    return result

x = 10
y = 4
print(substraction(x,y))



# 3. index and list 
'''
 list indexing refers to accessing elements within a list using their position, 
 where indexing starts at 0 for the first element, 1 for the second, and so on.
  
  '''
print()
print("-----3 -- index----position----")
print()


mylist = ["Joseph", "Xinwen","Claire","Seraphina", "Jennifer"]

print("The first person is ", mylist[0])
print("The second person is ", mylist[1])


# 4 .  built-in functions
'''
1) Python built-in functions are pre-defined functions available in the Python 
interpreter without requiring the import of any module
2)  These functions provide essential functionality for performing common 
    programming tasks across various domains
3) print()  
   len() return the length of a list of items
   max() return the largest item
   min() return the smallest item
   sum() return sum of items

'''
print()
print("-----4 -- built-in functions----")
print()

mylist = [1,2,3,4,5,6,10]
print("The length of mylist is ",len(mylist))
print("The largest value of mylist is ",max(mylist))
print("The smallest value of mylist is ", min(mylist))
print(" The sum of all values in mylist is ", sum(mylist))







