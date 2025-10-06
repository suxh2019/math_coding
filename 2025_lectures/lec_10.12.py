# -*- coding: utf-8 -*-
"""
Created on Sun Octomber 5, 2025

lecture on 10/12

@author: xihong
"""
print()
print()



# examples: a for loop combined with an if-else statement 

movies = ["harry", "Hermione ", "Albus", "Sirius", "Snape"]
for i in movies:
    if i == "harry":
        print("harry is found")
        break
else:
    print("harry is not found")   







print()
print()
# This example uses if-elif-else to classify each age into a category based on its value
ages = [78, 34, 21, 47, 9]
for age in ages:
    if age >= 55:
        print(age,"is a senior")
    elif age >= 35:
        print(age,"is middle aged")
    else:
        print(age,"is a youth")   