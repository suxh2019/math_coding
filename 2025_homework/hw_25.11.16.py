# -*- coding: utf-8 -*-
"""
Created on Sun 11/16 
homework for 11/16
@author: xihong
"""


'''
The tree code is from 
https://search.brave.com/search?q=python+code+for+christmas+tree++for+loops&summary=1&conversation=6703590ed5cfa8d8b50734
'''

print()
print("The holiday season is coming, make your own christmas tree-----")
def draw_tree(height):
    # Loop through each row of the tree
    for i in range(1, height + 1):
        # Print the spaces before the asterisks on each row
        for j in range(height - i):
            
            print(" ", end="")
        # Print the asterisks on each row
        for j in range(2 * i - 1):
            print("*", end="")
        # Move to the next line after each row
        print()

# Call the function to draw a tree with a height of 4
draw_tree(4)
draw_tree(4)



print()
print()



# Please look at the built-in functions from lec_25.11.16,
# Write the code for the questions below using built-in functions we learned


print()
print("-------Question 1-------")
print()
'''
 Given a list of numbers, assume that these numbers are increased by 10 or decresed by 10
 for example, the list can [10,20,30], or [40,30,20,10,0], or [100,110,120,130] and so on
 Given such a special list, write a function to find the second highest value 
in the list, return the second highest value
'''

# use the built-in function max(list) to find the largest value of the list

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
print("-------Question 2-------")
print()

'''
Given a list of numbers, assume that these numbers are increased by 10 or decresed by 10
for example, the list can [10,20,30], or [40,30,20,10,0], or [100,110,120,130] and so on
Given such a special list, write a function to find the second smallest value 
 in the list, return the second smallest value
'''

# use the built-in function min(list) to find the smallest value of the list

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
print("-------Question 3-------")
print()
'''
Write a function to compute the average of the grades
return the average grade
'''

# Use the built-in function len(list) to compute the length of the grades
# Use the built-in function sum(list) to compute the sum of the grades

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
print("-------Question 4-------")
print()

''' Count how many students in grade 6, return the count number'''

# use built-in function len(list) to get the number of students in each class, such as forest
# Use only ONE for loop, NOT double for loop


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



print()
print("-------Question 5-------")
print()

# What is definition/syntax of while loop in python? 
'''
Write your answer below.
-------------------------





-------------------------
Write your answer above.
'''



print()
print("-------Question 6-------")
print()

# What are difference between for loop and while loop in python? 
'''
Write your answer below.
-------------------------





-------------------------
Write your answer above.
'''


print()
print("-------Question 7-------")
print()

# What are similarities between for loop and while loop in python? 
'''
Write your answer below.
-------------------------





-------------------------
Write your answer above.
'''



