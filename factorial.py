# Date: 6/30/2025
# Calculate the factorial of a number


''' The code below is used to generate a sequence of numbers'''
print("The generated numbers in ascending order are as follows \n")
for k in range(1, 20,3):
    print(k)


print("The generated numbers in descending order are as follows \n")
for k in range(20, 1, -2):
    print(k)


''' cacluate the sum of numbers from 1 to 100'''
sum = 0
for k in range(1, 101):
    sum = sum + k
print("The sum of numbers from 1 to 100 is:  ",sum)
print("------------------")


''' Compute the factorial of number n'''
# Initialize the factorial value
factorial = 1
n = 5 
for i in range(1, n+1):
    factorial = factorial * i
print("factorial of ",n, " is:",factorial)

print("---------------")

''' Understand the difference between print inside the for loop and the print 
outside the for loop'''
mul = 1
for t in range(1, 3):
    print("mul inside the for loop ", mul)
    print("mul inside the for loop ", mul)
    
print("mul ourside the for loop ", mul)


print("-------------------------------")
'''Converts temperature from in Celsius unit to Fahrenheit unit.
 f =(c *9/5) + 32  
'''
def c_to_f(c):
  f = (c * 9/5) + 32
  return f

'''call the function'''
c = 37.7777
temp = c_to_f(c)
print("The temperature in fahrenheit is : ", temp)

'''Converts temperature from in Fahrenhei unit to celsius unit.
c= (f-32)*5/9'''

#define a function
def f_to_c(f):
  
  c=(f -32)*5/9
  return c

# call the function
f = 100
temp = f_to_c(f)
print("Temperature in Celsius is : ", temp)
 
    



