'''

Review the test taken on 1/11/2016 
1/18/2026
Xihong Su

'''

# (1) break

'''
break: 
    The break statement in Python is used to exit 
    a loop prematurely when a specific condition is met
'''

print()
''' Using break in a for loop '''
for letter in "math_coding":
    if letter == "_":
        break
    print("Current letter:", letter)
print("See you next time!")



print()
'''Using break in a while loop '''
value = -4
while True:
    print("current value is :", value)
    value = value + 1
    if value == 2:
        break
print("See you next time.")

# (2) list and indexing
'''
list and indexing:
    list:  collections of items enclosed in square brackets []
    Indexing:  accessing individual elements within a list by their position.
    
    Indexing starts at 0 for the first element,
    negative indices can be used to access elements from the end

'''
print()
names = ["Jennifer", "Claire", "Xinwen", "Joseph"]

print(names[0]) # output: Jennifer
print(names[1]) # output: Claire
print(names[2]) # output: Xinwen
print(names[3]) #output: Joseph

print(names[-1]) # output: Joseph
print(names[-2]) # output: Xinwen
print(names[-3]) # output: Claire
print(names[-4]) # output: Jennifer

'''
print(names[100]) # output: IndexError: list index out of range
print(names[6])  # output: IndexError: list index out of range
print(names[-10]) # output: IndexError: list index out of range
print(names[-5]) # output: IndexError: list index out of range
'''

# (3) range

'''
1) The step value CAN NOT be zero; it will raise a ValueError. 
    
2) The stop value is never included in the output, regardless of step direction

'''
# ValueError: range() arg 3 must not be zero
'''
for i in range(1,5,0):
    print(i)
'''



'''
The range() function allows you to generate sequences of numbers.

Positive Step Size
     1)the sequence increases from start to stop. 
     2)the sequence stops before reaching stop.
     3)If step is not specified, it defaults to 1.

'''
for i in  range(-4, 10, 3):
    print(i)

print()
'''
Negative Step Size
     1) the sequence decreases from start to stop. 
     2) the start must be greater than stop for the range to produce values.
     3)the sequence stops before reaching stop. 
    

'''
for i in range(6, 0, -2):
    print(i)




