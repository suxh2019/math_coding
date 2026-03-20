# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:00:21 2026

@author: xihong
"""

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


