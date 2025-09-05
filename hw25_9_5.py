# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 10:55:33 2025

@author: xihong
"""

# Calculate the factorial of n
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # recursive step
    else:
        return n * factorial(n - 1)
    
""" define a function"""
# f =(c *9/5) + 32  
def c_to_f(c):
  """Converts temperature from Celsius to Fahrenheit."""
  f = (c * 9/5) + 32
  return f

# call the function
c = 37.7777
temp = c_to_f(c)
print("temperature in fahrenheit is : ", temp)

# c= (f-32)*5/9
#define a function
def f_to_c(f):
  
  c=(f -32)*5/9
  return c

# call the function
f = 100
temp = f_to_c(f)
print("temperature in Celsius is : ", temp)

  
  









# mul =1
# for t in range(1,3):
#     print("testing")
#     print("testing")
    
# print("testing")






# Call a function given a temperature 40 Celsius
temp = c_to_f(40)
#Temp will return the temperature in unit fahrenheit
#print("temperature in Fahrenheit is:", temp)



















def fahrenheit_to_celsius(fahrenheit):
  """Converts temperature from Fahrenheit to Celsius."""
  celsius = (fahrenheit - 32) * 5/9
  return celsius
 
def addition(num1, num2):
    return num1 + num2

#practice: write code to get the sume of given three numbers
    
    
    
# The main function in Python is a convention used by programmers to define the starting point of a script. 
# def main():
#     num = 3
    
#     factorial_result =  factorial(num)
    
#     print("----------------------\n")
#     print("The factorial of", num, "is", factorial_result)
    
#     # print("Please enter two temperature in celsius")
#     # temp = float(input("Enter first number: "))
    
    
#     # print("Please enter two numbers for addtion")
#     # num1 = float(input("Enter first number: "))
#     # num2 = float(input("Enter second number: "))
#     # #sum = num1 + num2
#     # print("The sum of", num1, "and", num2, "is", addition(num1,num2))

# if __name__ == "__main__":
#     main()