# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 09:48:48 2026

@author: xihong

"""


# Recursion program analysis  -- 2

print()
print("------Drawing upside-down triangle of stars with Recursion--------------")
def stars_upside_down(n):
    if n == 1:
        print("*")
    else:
        print("*" * n)
        stars_upside_down(n - 1)

stars_upside_down(5)

print()
print("------Drawing triangle of stars with Recursion--------------")
def stars(n):
    if n == 1:
        print("*")
    else:
        stars(n - 1)
        print("*" * n)
stars(5)

print()
print("-------Factorial (Multiplying Numbers in a Fun Way) -------------")
#Factorial of 5 = 5 × 4 × 3 × 2 × 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("The factorial result is ", factorial(4)) 

"""
Difference between  loop and recursion

Loop → repeats using for or while
Recursion → a function calls itself


| Daily-life Example           | Recursion or Loop? | Why?                             |
| ---------------------------- | -----------------: | -------------------------------- |
| Russian dolls / nested boxes |      **Recursion** | Same action on a smaller thing   |
| Climbing down stairs         |      **Recursion** | Fewer stairs left each time      |
| Brushing teeth every day     |           **Loop** | Repeats over time                |
| Folders inside folders       |      **Recursion** | Search inside smaller folders    |
| Running laps on a track      |           **Loop** | Same circle repeats              |
| Countdown to launch          |      **Recursion** | Number gets smaller until 0      |
| Eating pancakes in a stack   |      **Recursion** | Smaller stack each time          |
| Seasons every year           |           **Loop** | Repeating cycle                  |
| Family tree                  |      **Recursion** | Same question on each generation |
| Washing dishes one by one    |      **Recursion** | Fewer dishes left each time      |


"""