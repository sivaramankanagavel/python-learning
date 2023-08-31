"""
How to define the function and let's see how to pass the parameter:
"""


# define the function:
def message(mes):  # mes --> as parameter
    print(mes)


message(mes="Hello World !")  # mes ---> as passing arguments


# creating the sum of the passing number:
def sum_of_num(num):
    addition_result = 0
    for i in range(0, num + 1):
        addition_result += i
    return addition_result


find_out_num = int(input("Enter an positive integer to find out the addition: "))
result_of_sum = sum_of_num(find_out_num)

print(f"The sum of num from 1 to {find_out_num}: {result_of_sum}")


# creating the function for return the total amount:
def total(num1, num2):
    return num1 + num2


print(total(20, 45))


# create function like n no of input without defining the parameters in the function
# (variable length parameters or arguments) this args is a tuple format:
def num_of_multiplication(*nums):  # *args
    total_result = 0

    for i in nums:
        total_result += i
    return total_result


print(num_of_multiplication(1, 2, 3, 5, 8, 56, 45))


# if you want to send the argument as a key & value pair means you don't need to declare each key as a parameter
# in the function instead you have to declare the **kwargs, this one is a dictionary type.

def print_address(**address):  # **kwargs as a dictionary type.
    for key, value in address.items():
        print(key + ": " + value)


print_address(door_no="238 e/1", street_name="north thittankulam", dist="tuticorin", state="tamilnadu", country="india")
