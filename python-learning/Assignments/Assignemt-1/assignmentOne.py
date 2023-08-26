"""
Here I am doing some assignment exercise and here we are going to solve
some problems.

1. get the input number n from the user and find the factorial for that one.
2. get the todo list data from the user and store it on the list of TODO.
3. get the integer values in List and process those data and findout the highest value with neighbor.
"""

# --- question - 1: Factorial ---#
# factorial_input = int(input("Enter the number to find out the factorial: "))
# factorial_result = 1
# for num in range(1, factorial_input+1):
#     factorial_result *= num
#
# print("Factorila Result: " + str(factorial_result))

# --- question - 2: TODO List from the USER ---#
# todo_list = []
# stop_loop_value = 1
#
# while stop_loop_value == 1:
#     todo_input = input("Enter the todo list here and we save it: ")
#     todo_list.append(todo_input)
#     stop_loop_value = int(input("Do you want add more todo in the List: "))
#
# print("The user added these todo: " + str(todo_list))

# --- question - 3: find out the highest neighbor value ---#
question_three = [3, 5, 9, 8, 4, 2]
highest_number = 0

for num in range(0, len(question_three)+1, 1):
    if(num  <= len(question_three) -1):
        if(highest_number < question_three[num]):
            highest_number = question_three[num]
        else:
            highest_number = question_three[num - 1]

print("Highest Number: " + str(highest_number))