# -*- coding: utf-8 -*-
"""
Created on 11/2
Exam for 11/9/2025

@author: xihong
"""

#------------keep the example code unchanged------------
print()
print("--------example--------")
# Write a function to compute the sum of two numbers, 
# function name: sum_numbers
# paramaters: num1, num2
# return the result

def sum_numbers(num1,num2):
    result = num1 + num2
    return result

# Call the function sum_numbers
a = 5
b = 6

res = sum_numbers(a, b)
print(a,"+", b , "=", res)
#------------keep the example code unchanged------------

print()
print("-------Question 1-------")
print()

# Write a function to compute the multiplication of two numbers, return the result
def mul(num1,num2):
    
    
    
    

    return 0


#------------keep the test code unchanged------------
# Call the function sum_numbers
a = 5
b = 6
res = mul(a, b)
print(a,"*", b , "=", res)
#------------keep the test code unchanged------------



print()
print("-------Question 2-------")
print()

# write a function to compute num1 * num2 + num3 and return the result
def mul_add(num1,num2,num3):
    
    
    
    
    
    return 0

#------------keep the test code unchanged------------
a = 5
b = 6
c =10
res = mul_add(a, b,c)
print(a,"*", b , "+",c,"=", res)
#------------keep the test code unchanged------------



print()
print("-------Question 3-------")
print()

# Write a function to count how many values that are equal to num in the list
# return the count number
def count_value(mylist,num):
    count = 0
    
 
    
    return count


#------------keep the test code unchanged------------
mylist_one = [1,10,2,10,5,6,10]
count_one = count_value(mylist_one,10)
print("How many 10 are in the mylist_one? ", count_one)
mylist_two = [1,2,1,2,2,2]
count_two = count_value(mylist_two,1)
print("How many 1 are in the mylist_two? ", count_two)
#------------keep the test code unchanged------------



print()
print("-------Question 4-------")
print()

# write a function to count how many people who are greater than num in the ages
# return the count number

def greater_than_num(ages,num):
    count = 0 
    
    
    
    
    return count


#------------keep the test code unchanged------------
ages = [0.5, 8, 34, 88,66,60]
seniors = greater_than_num(ages, 65)
print("There are",seniors, "senior people")

test = [11,12,90,99,95,80]
peo= greater_than_num(test, 80)
print("There are",peo, "people who are greater than 80 years old")
#------------keep the test code unchanged------------




print()
print("-------Question 5-------")
print()

# write a function to count how many people who are less than num in the ages
# return the count number
def less_than_num(ages,num):
    count = 0
    
    
    
    
    
    return count 

#------------keep the test code unchanged------------
ages_one = [0.5, 0.1,0.2, 78, 34]
baby_one = less_than_num(ages_one, 1)
print("There are",baby_one, "babies in the group one")

ages_two = [2,5,8,10,20,40]
kids = less_than_num(ages_two, 10)
print("There are",kids, "kids in the group two")
#------------keep the test code unchanged------------


print()
print("-------Question 6-------")
print()
# Given a list of numbers, assume that these numbers are increased by 10 or decresed by 10
# for example, the list can [10,20,30], or [40,30,20,10,0], or [100,110,120,130] and so on
# Given such a special list, write a function to find the second highest value 
# in the list, return the second highest value

def find_second_highest_value(list):
    
    
    
    
    
    
    return 0

#------------keep the test code unchanged------------
list_one = [10, 20, 30,40,50]
second_highest_value =  find_second_highest_value(list_one)
print("The second highest value in the first list is ", second_highest_value )
list_two = [120, 110, 100,90,80,70,60,50]
second_highest_value =  find_second_highest_value(list_two)
print("The second highest value in the second list is ", second_highest_value )
#------------keep the test code unchanged------------





print()
print("-------Question 7-------")
print()
# Given a list of numbers, assume that these numbers are increased by 10 or decresed by 10
# for example, the list can [10,20,30], or [40,30,20,10,0], or [100,110,120,130] and so on
# Given such a special list, write a function to find the second smallest value 
# in the list, return the second smallest value

def find_second_smallest_value(list):
    
    
    
    
    
    return 0
#------------keep the test code unchanged------------
list_one = [ 11, 21,31]
second_smallest_value =  find_second_smallest_value(list_one)
print("The second smallest value in the first list is ", second_smallest_value )

list_two = [1110, 1100, 1090,1080]
second_smallest_value =  find_second_smallest_value(list_two)
print("The second smallest value in the second list is ", second_smallest_value )
#------------keep the test code unchanged------------





print()
print("-------Question 8-------")
print()

# Write a function to compute the average of the grades
# return the average grade

def calculate_average_grade(grades):
    ave = 0
    
    
    
    
    return ave

#------------keep the test code unchanged------------
math_grades = [90,100,90,100,95]
avarege_math_grade = calculate_average_grade(math_grades)
print("The average math grade is: ",avarege_math_grade)

english_grades = [45, 40, 50, 45,45]
avarege_english_grade = calculate_average_grade(english_grades)
print("The average english grade is: ",avarege_english_grade)
#------------keep the test code unchanged------------


print()
print("-------Question 9-------")
print()

# Count how many students in grade 6, return the count number
def count_students(students):
   count  = 0
    
   
  
               
               
   return count

#------------keep the test code unchanged------------
forest = ["jessica","claire","joseph","xinwen","amber"]
ocean = ["jennifer","seraphina","richard","delta","sigma"]
river = ["abby","albert","grace","sony","chelsey"]

grade_six = [forest,ocean,river]
count = count_students(grade_six )
print("how many students are in grade six ? ", count)
#------------keep the test code unchanged------------

