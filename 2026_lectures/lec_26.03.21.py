# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:00:21 2026

@author: xihong
"""


# Selection sort

'''
Look at all the numbers, find the smallest one and put it in the first spot;
find the secobd smallest one and put it in the second spot;
Then repeat for the rest

'''
print()
print("------Selection sorting algorithm-------")
def selection_sort(arr):
    # arr =[64, 12, 22, 11]
    n = len(arr)  
    
    for i in range(n):
        min_index = i
        
        # Find the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example
numbers = [64, 12, 22, 11]
print(selection_sort(numbers))

'''
n = 4

i = 0
    min_index = 0
   j =1, arr[1] < arr[min_indxe]? 12< 64?  yes, min_index = 1
   j =2, arr[2] < arr[min_index]? 22<12? No
   j =3, arr[3] < arr[min_index]? 11 < 12? yes, min_index = 3
   swap arr[i] with arr[min_index], swap arr[0] with arr[3]
   
   Now, arr = [11,12,22,64]

i = 1
   min_index = 1
   j =2, arr[2] < arr[min_index]? 22<12? No
   j =3, arr[3] < arr[min_index]? 64< 22? no
   
   swap arr[i] with arr[min_index], swap arr[1] with arr[1]
   No change to the arr, arr = [11,12,22,64]
   
i = 2
   min_index = 2
   j = 3,  arr[3] < arr[min_index]? 64< 22? no
   swap arr[i] with arr[min_index], swap arr[2] with arr[2]
   No change to the arr, arr = [11,12,22,64]
         
i = 3
   for j in range(i+1, n):
       
  that is range(4,4), so the code block will not be executed
  
The final arr =  [11,12,22,64]

'''









# Play games to understand self-calling + base

# Game 1:
'''
🎲 1. “Call Yourself” Number Game

How it works:

Start with a number (e.g., 11).

A student says the number out loud.

Then “calls” the next student with number – 1.

Continue until reaching 0 (base case) → everyone says “STOP!”

Example flow:

Kid 1: “11 → calling 10”

Kid 2: “10 → calling 9”

…

Kid 5: “1 → calling 0”

Kid 6: “0 → STOP!”

Function calling itself

Base case (stopping condition)
'''



# Game 2:
'''
2. Russian Doll Drawing Activity
🎯 Goal: Visualize recursion

How it works:

Ask kids to draw a big shape (square or circle).

Inside it, draw a smaller version of the same shape.

Repeat 4–5 times until it gets tiny.

Discussion:

“What pattern do you see?”

“When did you stop drawing?”

Teach:

Same pattern repeating

“Smaller version of the same problem”

Base case = “too small to draw”

'''


print()
print("------Count down numbers-------")

def countdown(n):
    if n == 0:
        print("STOP!")
    else:
        print(n)
        countdown(n - 1)

countdown(11)



print()
print("------factorial-------")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(11))


