# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:51:13 2026

@author: xihong
"""
# Secion one: keywords continue and break
'''
Intuition of keyword continue:
    continue is like saying:
       “No thanks.”
       “Skip this one.”
       “Next!”
'''

'''
Comparison between break and continue: 
    
     continue = skip ONE thing
     break = stop EVERYTHING

'''



# Secion two: break and continue in a for loop
print()
print("****** Section two: break and continue in a for loop*******") 
print()
print("----output of using continue----")

foods = ["apple", "banana", "brocolli", "pizza", "fried dumpling", "fried rice"]
for food in foods:
    if food == "brocolli":
        continue
    print("Eat ", food)

print()
print("----output of using break----")
for food in foods:
    if food == "brocolli":
        break
    print("Eat ", food)

print("-----------------")
print()

print("------Skip Rainy Days------")
# Explanation: if it is rainy, skip outdoor play, continue to the next day

weather = ["sunny", "rainy", "sunny", "cloudy"]
for day in weather:

    if day == "rainy":
        continue

    print("It is a", day, "day! Let's play outside!")
    

# Section three: break and continue in a while loop
print()
print("****** Section three: break and continue in a while loop******")  
    
# Use break
print()
print("--------break--------")
energy = 5
while energy > 0:
    print("Playing game")
    energy = energy - 1
    if energy == 0:
        break   
    
# Use continue
print()
print("------- continue--------")
energy = 5
while energy > 0:
    energy = energy - 1
    if energy == 2:
        print("Too tired... skip this turn")
        continue

    print("Playing game! Energy:", energy)

  