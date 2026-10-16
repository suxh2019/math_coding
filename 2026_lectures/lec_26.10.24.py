# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:58:25 2026

@author: xihong
"""

# Permutation
'''
(1) A permutation is an arrangement of items 
where order matters
(2) Given mylist = [1, 2, 3], what are permuations?
[1, 2, 3],[1, 3, 2],[2, 1, 3]
[2, 3, 1],[3, 1, 2],[3, 2, 1]
'''
# Question 1: so for n distinct items, the 
# number of permutations is:

# write your answer down below and explain it


print()
print("----list operations----")
# List operations:
nums = [1, 2, 3, 11, 22, 44]

# append() adds the whole object as one element.
nums.append(4)
print("Append :",nums) # [1, 2, 3, 4]  
print()

# insert(index, value) adds an item at a specific position
nums.insert(1, 10)
print("Insert: ",nums) # [1, 10, 2, 3, 4]

# copy() creates a shallow copy of a list
new_nums = nums.copy()
print("copy: ", new_nums) # [1, 2, 3]
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

print("----Code Explaination----")
# Discuss the code and explain how it works
numbers = ["B", "C"]
new_letter = "A"

for position in range(3):
    new_list = numbers.copy()
    new_list.insert(position, new_letter)

    print("Put A at position", position, ":", new_list)

 
