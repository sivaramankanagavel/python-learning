# find square number up to the passing value:

def find_square_generator(num):
    for iterable in range(0, num + 1):
        yield iterable * iterable


# Recursion:

def find_recursion(num):
    if num == 0:
        return 1
    return num * find_recursion(num - 1)