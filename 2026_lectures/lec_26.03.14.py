# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:04:34 2026

@author: xihong
"""

mylist = [3,6,19,4,20,1]

print()
print("----------Print the value from left to right------------")

for i in range(0,len(mylist)):
    print(mylist[i])

print()
print("--------print the value from right to left--------------")
print("---negative index---")

for i in range(1,len(mylist)+1):
    print(mylist[-i])

print()
print("--positve index, backward---")
for i in range(len(mylist)-1, -1, -1):
    print(mylist[i])


print()
print("-----print the first five numbers in the list of numbers_one-----")

numbers_one = [1,2,3,4,6,8,6,10,100,23,45,21,22,32,43,44]

for i in range(0,5):
     print(numbers_one[i])
    


print()
print("-----print the last five numbers in the list of numbers_one-----")

numbers_one = [1,2,3,4,6,8,6,10,100,23,45,21,22,32,43,44]

for i in range(1,6):
     print(numbers_one[-i])