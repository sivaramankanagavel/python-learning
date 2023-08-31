"""
Add the 10-peoples favorite food and names into the dictionary and sorted the foods based on the most-liked.
"""

# Dictionary and List Exercise:

user_details_wrap = []

for i in range(1, 3):
    user_details = {}
    user_name = input("Enter your name: ")
    user_fav_food = input("Enter your favorite food: ")
    user_details["Id"] = i
    user_details["user_name"] = user_name
    user_details["favorite_food"] = user_fav_food
    user_details_wrap.append(user_details)

print(user_details_wrap)

# Dictionary Exercise 2:
user_data_base = []

for i in range(1, 3):
    user_details = {}
    user_fav_food_list = []

    user_name = input("Enter your name: ")
    user_fav_food_list.append(input("Enter your favorite food: "))

    user_more_food = input("Do you want to enter a more food Y or N: ")

    while user_more_food == "Y":
        user_fav_food_list.append(input("Enter your favorite food: "))
        user_more_food = input("Do you want to enter a more food Y or N: ")

    user_details["Id"] = i
    user_details["User_name"] = user_name
    user_details["Fav_food"] = user_fav_food_list

    user_data_base.append(user_details)

print(user_data_base)