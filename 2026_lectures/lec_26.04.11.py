# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:51:33 2026

Understand how the recursion program works

@author: xihong


1. Motivation of using recursion:
    Recursion helps us solve big problems by breaking them into 
    smaller versions of the same problem.
    
2. Main idea of recursion:
   Instead of solving everything at once, we say:
   “Can I solve a smaller version first?”
   “Then use that answer to solve the bigger one.”
   

3. Recursion = when something does a smaller version of itself again and 
   again until it reaches a stopping point.

   Every recursion needs a stopping point (called the base case), or it will go forever!
4. Daily examples of recursion:
    (1) Eating a stack of pancakes
        How do you eat 5 pancakes?

       Eat the top pancake
       Now you have 4 pancakes left
       Do the same thing again
       Stop when no pancakes are left 😄

    (2) Climbing down stairs
       If you are on stair 5:

       Step down one stair
       Now you are on stair 4
       Do the same thing again
       Keep going until stair 0
    (3) Mirrors facing each other

      When two mirrors face each other, you see:
       image inside image inside image...
       This looks like recursion because the pattern repeats itself.

"""

# Recursion program analysis  -- 1

#The execution flow is shown in lec_26.04.11.pdf


print()
print("-------Counting Down with Recursion-------------")

def countdown(n):
    if n == 1:
        print("Base case, stop!")
    else:
        print(n)
        countdown(n - 1)  # function calls itself

countdown(5)


print()
print("----Counting Down with Recursion----------------")

def countdown(n):
    if n == 0:
        print("Base case, stop!")
    else:
        
        countdown(n - 1)  # function calls itself
        print(n)

countdown(5)







