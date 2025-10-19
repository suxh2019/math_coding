# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 
homework for 10/26
@author: xihong
"""

# write a function to count the number of students whose name is name

'''
hints: 1) use double for loop and one if statement 
       2) Use outer for loop to read class names from grades
       3) Use inner for loop to read each student's name from each class
       4) compare if the student's name is equal to name. if yes, then count is 
       increased by one; if no, do nothing
       5) return count
'''
def count_duplicated_name(grades,name):
   
    # Use count to keep track of the number of students whose names are name
   count = 0
    
  
               
               
   return count    
    
   
    
   


# three classes: forest, ocean,and river
# each class has several students
forest = ["jessica","claire","joseph","xinwen","amber"]
ocean = ["jennifer","seraphina","sorephena","jessica","sophrina"]
river = ["joseph","jessica","abby","albert","grace","jessica"]

# Grade six has three classes
grade_six=[forest,ocean,river]

# call the function "count_dupilcated_name" and compute how many students 
# in grade six have the name jessica
count = count_duplicated_name(grade_six, "jessica")

print()
# print the number
print("how many students whose names are jessica? ", count)



