# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:05:41 2026

@author: xihong
"""

'''
String:
    (1) A string in Python is a piece of text.
    (2) create a string by putting text inside quotes:
'''
print("----------------")
name = "Jessica"
message = "Hello"
print("The first letter of the name ",name[0])
print("The last letter of the message ", message[-1])

#These are strings because they contain text.
print()
print("-----type-----")
#Strings can also contain numbers, 
#as long as the numbers are inside quotes:
    
age = "13" # "13" is a string, not a number
age_num = 13

print(type(age ))
print(type(age_num))

print()
print("----join strings----")
# You can also join strings:  
first = "Hello"
second = "World"

print(first + " " + second) 
  
print()
print("--length---")  

word = "Python"
print(len(word))

#Repeat a string
print()
print("--repeat a string---")
print("Hi! " * 3)

# Use .upper()
print()
print("--Uppercase---")
word = "python"
print(word.upper())

#Check if a word contains a letter
print()
print("------")
word = "banana"

if "a" in word:
    print("Yes")

print()
print("------")
# input() in Python is used to ask the user 
# to type something.
# name = input("What is your name? ")
# print("Hello,", name)

print("-----------")
print("Question 1")
'''
Write a Python program that:

Asks the user for their name.
Asks the user for their favorite color.
Prints a sentence like:
'''


 


print("-----------")
print("Question 2") 
'''
Given a string word and a letter target, 
count how many times target appears in word.

Example:
    word = "banana"
    target = "a"
output: 3
'''

def count_letter(word, target):
    count = 0
    # write your code below
    

    return count


print(count_letter("banana", "a"))






  