"""
Higher order function is nothing but a which function receives the function as a parameter or else return the another
function is called Higher Order Function.
"""


def happy():
    print("Happy....")


def sad():
    print("Sad.....")


def higher_order_function(func):
    func()
    return sad


higher_one = higher_order_function(happy)
higher_one()
