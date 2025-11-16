
"""
9/5/2025
Homework: addition, multiplciation, subtraction, division,power

@author: xihong
"""


# addition of two numbers
def addition(num1, num2):
    result = num1 + num2
    return result

'''
Write code to do the subtraction
result = num1 - num2
'''
def subtraction(num1, num2):
    
    return 0 # 0 needs to be replaced with by other variable, something like result in addition


'''
Write a code to do the multiplication
result = num1 *  num2, similar to addition and subtraction
function name is multiplication
'''




'''
Write a code to do the division
result = num1 /  num2, similar to addition and subtraction
function name is division
'''



'''
Write a code to do the addtion of three numbers
result = num1 + num2 + num1, 
'''
def addition_three_numbers(num1,num2,num3):
    result = num1 + num2 + num3
    return result




a = 20
b = 5
c =25

sum = addition(a,b)
print("a + b = ", sum)

minus = subtraction(a,b)
print("a - b = ", minus) 

'''
multip = multiplication(a,b)
print(" a * b = ", multip)

div= division(a,b)
print(" a / b = ", div)
'''


sum_three_number = addition_three_numbers(a, b, b)
print("a + b + c = ", sum_three_number)

