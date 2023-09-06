"""
We are going to create the guessing number game using random package
"""

import random

random_number = random.randint(1, 10)

input_from_user = int(input("Enter The guessing number between 1 to 10: "))

while input_from_user != random_number:
    if input_from_user > random_number:
        print("The guessing number is higher")
    else:
        print("The guessing number is lower")
    input_from_user = int(input("Enter Again: "))

print("You win the game")