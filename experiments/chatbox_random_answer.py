# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:52:22 2026

@author: xihong
"""

# Simple Chat Box for Kids
# The computer gives random answers

import random

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

# List of random answers
# Feel free to add more answers
answers = [
    "That sounds fun!",
    "Wow, really?",
    "I like that idea!",
    "Can you tell me more?",
    "Cool!",
    "Haha, that's funny!",
    "I am still learning!",
    "Great question!",
    "Awesome!",
    "Let's play again!"
]

print("🤖 Kid Chat Box")
print("Type 'bye' to stop.\n")

# Keep chatting forever
while True:
    
    # Ask the user to type something
    user_message = input("You: ")

    # Stop the chat if user types bye
    if user_message.lower() == "bye":
        print("Robot: Goodbye!")
        break

    # Pick a random answer
    robot_reply = random.choice(answers)

    # Show the answer
    print("Robot:", robot_reply)