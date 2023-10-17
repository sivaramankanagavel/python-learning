from mathModule.math_operations import find_square_generator
from mathModule.math_operations import find_recursion

square_value = find_square_generator(10)
for i in square_value:
    print(i)

recursion_value = find_recursion(5)
print(recursion_value)