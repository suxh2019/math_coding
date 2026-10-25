# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:58:25 2026

@author: xihong
"""

print()
print("----list operations----")
# List operations:
nums = [1, 2, 3, 11, 22, 44]

# insert(index, value) adds an item at a specific position
nums.insert(1, 10)
print("Insert: ",nums) # [1, 10, 2, 3, 4]

# copy() creates a shallow copy of a list
new_nums = nums.copy()
print("copy: ", new_nums) # 
print()

#A shallow copy means you create a new outer 
#list, but the objects inside it are still shared.
a = [1, 2, 3]
b = a.copy()
# Now a and b are different list objects:
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
# So changing the outer list b does not change a.
print()


# Remove and return the last item:
x = nums.pop()
print("The popped element: ", x)
print("The list after popping the last element: ", nums)
print()

# Remove at a specific index
y = nums.pop(1)
print("The popped element: ", y)
print("The list after popping the last element: ", nums)
print()

'''
A slice lets you take part of a Python list
The basic syntax is: list[start:stop]
start is included
stop is not included
'''
print("Slice of the nums: ",nums[1:3])

#You can omit start
print("Omit start: ",nums[:4])

# Omit stop
print("Omit stop: ",nums[2:])
print()

print("-----dictionary----") 

'''
Given a dictionary where each key is a student's ID and 
each value is their math test score, write a for loop to
print student's ID and the math test score
'''
math_scores = {
    101: 85,
    102: 92
}

scores =[]
ids = []
for id,score in math_scores.items():
    ids.append(id)
    print("The student ID is ", id)
    scores.append(score)
    print("The math score is ",score)
print("Scores are ", scores)
print("ids are ", ids)
print()

print("--quotes---")
'''
(1) Python allows both single quotes (' ') and 
double quotes (" ") to define strings;
(2) In Python, a character is defined as a string containing 
exactly one character. For example, 'A' is a str containing 
one character.
(3) Python usually displays strings in lists using single 
quotes, even if you originally used double quotes.

'''
list1 = ['Elaine', 'Jennifer']
list2 = ["Elaine", "Jennifer"]
print(list1 == list2)
   
print()
# Question 1:Find Students Born in a Specific Year
# Topic: Dictionaries, String Slicing, Loops, and Conditional Statements
'''
You are given a dictionary called students, 
where each key is a student's name and each value 
is the student's birthday in the 
format "YYYY-MM-DD" (year-month-day).
Write a Python function 
students_by_year(students, target_year) that finds 
all students who were born in a specified year.
'''
# Hint: if target_year is "2013", 
#output = ['Elaine','Jennifer']

# Solution 1
def students_by_year(students, target_year):
    output =[]
    for student,birth in students.items():
        year = birth[0:4]
        if target_year ==year:
            output.append(student)
            
    return output

print()
print("----test case solution 1----")
students = { 
    "Alice": "2014-05-12",
    "Bob": "2013-11-25",
    "Elaine": "2015-02-08",
    "David": "2013-06-17",
    "Emma": "2014-09-03",
    "Xinwen": "2013-04-21",
    "Joseph": "2014-01-21",
    "Claire": "2014-03-21",
    "Jennifer": "2015-06-21"
} 
res2013 = ",".join(students_by_year(students, "2013"))
print("Students who were born in 2013 are:" ,res2013)
print()
res2014 = ",".join(students_by_year(students, "2014"))
print("Students who were born in 2014 are:" ,res2014)
print()
res2015 = ",".join(students_by_year(students, "2015"))
print("Students who were born in 2015 are:" ,res2015)
print()

# Solution 2
def students_by_year_solution2(students, target_year):
    output =[]
    for student,birth in students.items():
        if target_year in birth:
            output.append(student)
            
    return output

print()
print("----Solution 2--test case----")
students = { 
    "Alice": "2014-05-12",
    "Bob": "2013-11-25",
    "Elaine": "2015-02-08",
    "David": "2013-06-17",
    "Emma": "2014-09-03",
    "Xinwen": "2013-04-21",
    "Joseph": "2014-01-21",
    "Claire": "2014-03-21",
    "Jennifer": "2015-06-21"
} 
res2013 = ",".join(students_by_year_solution2(students, "2013"))
print("Students who were born in 2013 are:" ,res2013)
print()
res2014 = ",".join(students_by_year_solution2(students, "2014"))
print("Students who were born in 2014 are:" ,res2014)
print()
res2015 = ",".join(students_by_year_solution2(students, "2015"))
print("Students who were born in 2015 are:" ,res2015)
print()


 
