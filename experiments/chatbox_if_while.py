# -*- coding: utf-8 -*-
"""
Created on Sun May 10 07:15:33 2026

@author: xihong
"""

# Multiple Users Chat Login System

# Store usernames and passwords
users = {
    "Claire": "1111",
    "Joseph": "2222",
    "Xinwen": "3333",
    "Jennifer": "4444"
}

print("Welcome to Super Chat Bot!")

# Login loop
while True:
    username = input("Username: ")
    password = input("Password: ")
   # Check if username exists
    if username in users:

        # Check password
        if users[username] == password:
            print("Login successful!")
            break

    print("Wrong username or password. Try again.")

# Chat starts
print("You can now chat with the robot!")
print("Type 'bye' to leave.")

while True:

    message = input(username + ": ")

    if message == "bye":
       print("Robot: Goodbye!")
       break

    elif message == "hello":
       print("Robot: Hi", username + "!")

    elif message == "how are you":
        print("Robot: I am happy!")

    elif message == "what is your name":
        print("Robot: My name is Robo!")

    elif message == "favorite food":
        print("Robot: I like pizza!")

    elif message == "joke":
        print("Robot: Why did the cat sit on the computer? To keep an eye on the mouse!")
    # you can add more messages, such as
    # elif message == "favorite movie":
    #     print("Robot: I like Snow White!")

    else:
        print("Robot: That sounds interesting!")