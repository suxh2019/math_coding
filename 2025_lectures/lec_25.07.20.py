# -*- coding: utf-8 -*-
"""
For loop

@author: xihong
"""

#variable

'''
A variable:
   (1) a symbolic name that refers to a value
   (2) create a variable by assigning a value to it 
       using the assignment operator (=)

'''

# Variable examples

i = 10
x = 3 
y = 5
name = "chacha"


# for loop

'''
  1. A control flow statement designed to iterate over a sequence of elements,
      such as a list
  2. The loop continues until all items in the sequence have been processed
  3. syntax:
      (1) for : keyword
      (2) a loop variable
      (3) in : keyword
      (4) iterable object, such as a list
      (5) ending with a colon
      (6) The code block must be indented

  4. Example:
      foods = [candy, ice_cream,noodle]
      for food in foods:
          print(food)
     
     In the above example, food is the loop variable, foods in the iterable 
     object, print(food) is the code block

'''



'''
range() function is used to generate a sequence of numbers
 
range(start, stop)
   1) the sequence begins at start parameter
   2) the sequence is increased by 1
   3) stop parameter is required and specifies the upper limit of the sequence
   4) stop value is not included in the output
   
 
'''
print()
print("-----sequence is increased by 1--------")
# Print numbers 1,2,3,4
for i in range(1,5):
    print(i)

'''
 
range(start, stop, step)
   1) the sequence begins at start parameter
   2) the sequence is increased by step
   3) stop parameter is required and specifies the upper limit of the sequence
   4) stop value is not included in the output
   
 
'''
print()
print("-------sequence is increased by 2------")
# Print numbers 1,3,5,7
for i in range(1,8,2):
    print(i)
    
print()
print("-------sequence is increased by 4------")
# Print numbers 1,5,9,13,17
for i in range(1,20,4):
    print(i)
    
    
 
  



