# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 09:16:06 2026

@author: xihong
"""

def count_duplicated_name(grades,name):
   
    # Use count to keep track of the number of students whose names are name
   count = 0
   
  
               
               
   return count    
    
   
    
   


# three classes: forest, ocean,and river
# each class has several students
forest = ["jessica","claire","fakename","joseph","xinwen","amber","fakename"]
ocean = ["jennifer","fakename","fakename","jessica","fakename"]
river = ["joseph","fakename","jessica","abby","albert","grace","jessica"]

# Grade six has three classes
grade_six=[forest,ocean,river]

# call the function "count_dupilcated_name" and compute how many students 
# in grade six have the name fakename
count = count_duplicated_name(grade_six, "fakename")

print()
# print the number
print("how many students whose names are fakename? ", count)


print("--------------------")

# Question 2: write the code to swap three variable values
# x =1, y =100, z =1000; Finish the rotation code below
# After the rotation:x =100, y=1000,z=1
# Hint:swap two variable each time

def rotate_three_values(x,y,z):
   
    
    
    
     return x,y,z



x = 1
y = 100
z = 1000
print()
print("-------Before the rotation-------------")
# output x =  1  y =  100  z =  1000
print("x = ", x, " y = ",y, " z = ",z) 

print()
print("--------After the rotation------------")

xnew,ynew,znew = rotate_three_values(x,y,z)

# output: xnew =  100  ynew =  1000  znew=  1
print("xnew = ", xnew, " ynew = ",ynew, " znew= ",znew)

