# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:34:43 2026

@author: xihong
"""

# Store usernames and passwords
users = {
    "Claire": "1111",
    "Joseph": "2222",
    "Xinwen": "3333",
    "Jennifer": "4444"
}

print("Welcome to Super Calculator!")

# Login loop
while True:
    username = input("Username: ")
    password = input("Password: ")
   # Check if username exists
    if username in users:

        # Check password
        if users[username] == password:
            print("Master", username," I am ready to serve you!")
            break

    print("Wrong username or password. Try again.")


print("Type 'bye' anytime to stop.")

while True:

    first = input("Enter first number: ")

    # Stop calculator
    if first == "bye":
        print("Goodbye!")
        break

    second = input("Enter second number: ")

    if second == "bye":
        print("Goodbye!")
        break

    # Change text into numbers
    first = float(first)
    second = float(second)

    print("Choose an operation:")
    print("+  Add")
    print("-  Subtract")
    print("*  Multiply")
    print("/  Divide")

    operation = input("Operation: ")

    # Math operations
    if operation == "+":
        answer = first + second
        print("Answer =", answer)

    elif operation == "-":
        answer = first - second
        print("Answer =", answer)

    elif operation == "*":
        answer = first * second
        print("Answer =", answer)

    elif operation == "/":

        if second == 0:
            print("Cannot divide by zero!")

        else:
            answer = first / second
            print("Answer =", answer)

    else:
        print("Unknown operation!")