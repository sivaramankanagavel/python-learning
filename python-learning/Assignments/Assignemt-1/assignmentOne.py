"""
Here I am doing some assignment exercise and here we are going to solve
some problems.

1. get the input number n from the user and find the factorial for that one.
2. get the todo list data from the user and store it on the list of TODO.
3. get the integer values in List and process those data and findout the highest value with neighbor.
4. list [3, 5, 7, -2, -1, 10, 8, 6] make the all negative numbers in the end of list.
"""

# --- question - 1: Factorial ---#
factorial_input = int(input("Enter the number to find out the factorial: "))
factorial_result = 1
for num in range(1, factorial_input+1):
    factorial_result *= num

print("Factorila Result: " + str(factorial_result))

# --- question - 2: TODO List from the USER ---#
todo_list = []
stop_loop_value = 1

while stop_loop_value == 1:
    todo_input = input("Enter the todo list here and we save it: ")
    todo_list.append(todo_input)
    stop_loop_value = int(input("Do you want add more todo in the List: "))

print("The user added these todo: " + str(todo_list))

# --- question - 3: find out the highest neighbor value ---#
question_three = [3, 7, 9, 11, 15]# [3, 5, 9, 8, 4, 2]
highest_number_one = 0

if len(question_three) % 2 == 0:
    for num in question_three:
        if highest_number_one < num:
            highest_number_one = num
        else:
            continue

else:
    for index, num in enumerate(question_three):
        if index != len(question_three) - 1:
            if highest_number_one < num:
                highest_number_one = num
            else:
                continue

print("Highest Number: " + str(highest_number_one))

# --- question - 4: make the negative numbers in the List at last ---#
new_positive_array = []
new_negative_array = []

test_array = [5, 7, 9, -5, -12, -2, 6, 12]

for num in test_array:
    if num > 0:
        new_positive_array.append(num)
    else:
        new_negative_array.append(num)

final_result_negative_last = new_positive_array + new_negative_array
print(final_result_negative_last)

final_result_negative_last.sort(reverse=True)

print(final_result_negative_last)
