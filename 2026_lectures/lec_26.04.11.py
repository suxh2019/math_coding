# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:51:33 2026

Understand how the recursion program works

@author: xihong
"""
print()
print("-------Counting Down with Recursion-------------")

def countdown(n):
    if n == 0:
        print("Base case, stop!")
    else:
        print(n)
        countdown(n - 1)  # function calls itself

countdown(4)


print()
print("----Counting Down with Recursion----------------")

def countdown(n):
    if n == 0:
        print("Base case, stop!")
    else:
        
        countdown(n - 1)  # function calls itself
        print(n)

countdown(4)


print()
print("-------Factorial (Multiplying Numbers in a Fun Way) -------------")
#Factorial of 5 = 5 × 4 × 3 × 2 × 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("The factorial result is ", factorial(4)) 


print()
print("------Drawing Stars with Recursion--------------")
def stars(n):
    if n == 0:
        return
    print("*" * n)
    stars(n - 1)

stars(5)






