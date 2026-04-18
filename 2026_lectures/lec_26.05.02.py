# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:26:55 2026

@author: xihong
"""

'''
Fibonacci (pattern game): 
    Each number = sum of previous two

'''

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))








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