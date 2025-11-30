# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 14:02:37 2025

@author: xihong
"""

print()
print("-------question 1------------")
 # write a while loop to compute the sum of numbers from 1 to n, n can be any number
def sum_numbers(n):
    result_sum = 0
   
    
   
    
    return result_sum


print()
print("-----keep the test code unchanged-----")
sum1 = sum_numbers(10)
print("1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = ", sum1)
sum2 = sum_numbers(100)
print("1 + 2 + ... + 99 + 100 = ", sum2)
sum3 = sum_numbers(5000)
print("1 + 2 + 3 + ... + 4999 + 5000 =  ", sum3)
print("-----keep the test code unchanged-----")



print()
print("-------question 2------------")
# write a while loop to do the multiplication of numbers from 1 to n

def multiplication(n):
   result_multi = 1
   
   
   
   
   return result_multi

print()    
print("-----keep the test code unchanged-----")
mul1 = multiplication(5)
print("1 * 2 * 3 * 4 * 5 =", mul1)
mul2 = multiplication(100)
print("1 * 2 * 3 * ... * 99 * 100 = ", mul2)
mul3 = multiplication(500)
print("1 * 2 * 3 * ... * 499 * 500 =  ", mul3)
print("-----keep the test code unchanged-----")


print()
print("-------question 3------------")
# use if-elif-else to give letter to a student's grade
'''
0  <=  grade < 60 ; letter: F
60 <=  grade < 70; letter: D
70 <=  grade < 80 ; letter : C
80 <=  grade < 90 : letter: B
90 <=  grade < 100 ; letter : A
grade:100; letter:E

'''

# Please write the code to include all cases above
def assign_grade_letter(grade):
   if 0 <= grade < 60:
       return "F"
   #elif 








print()    
print("-----keep the test code unchanged-----")
lec1 = assign_grade_letter(34)
print("score 34 =>  ", lec1)
lec2 = assign_grade_letter(65)
print("score 65 =>  ", lec2)
lec3 = assign_grade_letter(75)
print("score 75 =>  ", lec3)
lec4 = assign_grade_letter(85)
print("score 85 =>  ", lec4)
lec5 = assign_grade_letter(95)
print("score 95 =>  ", lec5)
lec6 = assign_grade_letter(100)
print("score 100 =>  ", lec6)
print("-----keep the test code unchanged-----")