# -*- coding: utf-8 -*-
"""
Created on Sun Octomber 5, 2025

lecture on 10/12

Purpose: pratice a for loop combined with an if-else statement 

@author: xihong
"""
print()
print()





# No duplicates in the list
movies = ["harry", "Hermione ", "Albus", "Sirius", "Snape"]
for i in movies:
    if i == "harry":
        print("harry is found")
        break
    else:
        print("harry is not found")   





print()
#This function takes a list lst as an argument/parameter and 
#returns the number of times the integer 10 appears in it. 

def count_10(mylist):
    
    
    
    
    
    # 0 needs to be replaced by a 
    # variable that represents the times of 10 occurs in the list
    return 0


# Duplicates in the list
mylist = [1,10,2,10,5,6,10,7,11]
count = count_10(mylist)
print("How many 10 in the list? ", count)
 



'''
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
'''