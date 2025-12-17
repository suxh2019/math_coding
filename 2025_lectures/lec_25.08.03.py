# -*- coding: utf-8 -*-
"""
For loop and range() function

@author: xihong
"""

'''
 
range(start, stop, step)
   1) the sequence begins at start parameter
   2) the sequence is increased by step
   3) stop parameter is required and specifies the upper limit of the sequence
   4) stop value is not included in the output
   
 
'''
    
    
print()
print("-------sequence is decreased by 1------")
# Print numbers 6,5,4,3,2
for i in range(6,1,-1):
    print(i) 
    
print()
print("-------sequence is decreased by 2------")
# Print numbers 6,4,2
for i in range(6,1,-2):
     print(i)  



 
print()
print("-------print numbers ------")

numbers = [1,11,111,22,33]
for i in numbers:
    print(i)

 
  
print()
print("-------names------")
names = ["Jennifer","Joseph","Seraphina","Claire","Xinwen"]
for name in names:
    print(name)
  
    
print()
print("-------print each movie twice ------")
movies = ["Harry Potter","Snow White"]
for movie in movies:
    print(movie)
    print(movie)




