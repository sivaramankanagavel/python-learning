import math
"""
Here we are doing some math operation like addition, subtraction, multiplication, division and so on.

math module is used to fetch the defined function from this module to use explicitly and these function
are like a ceil, floor, factorial and gcd so on.
"""

value_one = 10
value_two = 50
value_three = 5
value_four = 2
value_five = 8.435
value_six = 8.7432
value_seven = 8.5
value_eight = 8.567

value_nine = 45.55
value_ten = 45
value_leven = 3
value_twelve = 6

"""Addition"""
print(value_one + value_two)

"""Subtraction"""
print(value_one - value_three)

"""Multiplication"""
print(value_two * value_four)

"""Division"""
print(value_two / value_four)

"""Floor Division it gives the result in next nearest INT number"""
print(value_two // value_three)

"""Modulus"""
print(value_three % value_four)

"""round method to convert the given float value into nearest value of the next integer we return it"""
print(round(value_five))
print(round(value_six))
print(round(value_seven))
print(round(value_eight))

"""absolute method was used to change the negative values into positive number"""
print(abs(-10.05))
print(abs(-5.5))

"""pow method was used to find out the power of the given value"""
print(pow(10, 2))
print(pow(5.5, 3))
print(pow(5, 3))
print(5**3)

"""To find out the maximum and minimum value"""
print(max(value_nine, value_ten))
print(min(value_nine, value_leven))

"""Ceil, floor and factorial"""
print(math.ceil(value_nine))
print(math.floor(value_nine))
print(math.factorial(value_three))

#--- logarithm, cosine value and e^n ---#
"""Logarithm"""
logarithm_value = input("Enter an number to find out the logarithm: ")
base_value = input("Enter a base value: ")
print(math.log(float(logarithm_value), float(base_value)))

"""cosine"""
value_cosine = math.radians(45)
cosine_result = math.cos(value_cosine)
print(cosine_result)

"""e^n e=2.71828"""
value_exp = math.exp(5.5)
print(value_exp)
