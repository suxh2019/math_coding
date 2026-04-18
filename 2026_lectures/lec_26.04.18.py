# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 09:48:48 2026

@author: xihong

"""


# Recursion program analysis  -- 2
# Please look at lec_26.04.18.pdf to better understand how recursion programs work

print()
print("------Drawing upside-down triangle of stars with Recursion--------------")
def stars_triangle_upside_down(n):
    if n == 1:
        print("*")
    else:
        print("*" * n)
        stars_triangle_upside_down(n - 1)

stars_triangle_upside_down(5)

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
#Factorial of 4! = 4 × 3 × 2 × 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("The factorial result is ", factorial(4)) 

