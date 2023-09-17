"""
Lambda expression is using to write the single line function which function are return some simple operation result
those function are make it as a Lambda function.

And Lambda is called as an anonymous function due to we are not assign this lambda function into any variables in real
time so, we just passing this lambda as an parameter to an Higher-Order-Function.

Example:
    def add_num(num):
        return num + 10

    add_num(5) // result --> 15

    adding_result = lambda num1, num2, num3, ....numN: num1 + 10
    adding_result(5, 10, 15, 20, ...N)
"""


# Normal Function for adding some values:
def add_num(num):
    return num + 8


print(add_num(10))


# Lambda Expression:
adding_result = lambda num: num + 10
print(adding_result(10))

multiplication_result = lambda a, b, c: a * b * c
print(multiplication_result(5, 6, 4))

strong_enough = lambda w: "Yes" if w > 65 else "No"
print(strong_enough(66))
print(strong_enough(64))