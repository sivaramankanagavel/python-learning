"""
Here we are going to learn the format method in depth
"""

# format():

format_value_one = "Hi {}"
format_value_two = "the pi value is {}"
format_value_three = 34555566
format_value_four = "the number was starts from {0}, {1}, {2}"
format_value_five = "the pi value is {:.3f}"
format_value_six = 400

# format()
print(format_value_one.format("Siva"))

# based on the index we defined in the string:
print(format_value_four.format(1, 4, 6))

# doing the round and minimizing the digit need to print on the string:
print(format_value_two.format(3.14156))
print(format_value_five.format(3.14156))
# comma separation with the large number digit:
print("The num is {:,} ".format(format_value_three))
print("*****{}******".format("Welcome"))

# Padding:
print("*****{:20}******".format("Welcome"))
# padding left:
print("*****{:>20}******".format("Welcome"))
# padding right:
print("*****{:<20}******".format("Welcome"))
# padding center:
print("*****{:^20}******".format("Welcome"))

# formatting the number into binary(b), octal(c), hexa(x or X) and E for scientific notation:
print("the binary value is {:b}".format(format_value_six))
print("the octal value is {:o}".format(format_value_six))
print("the hexa value is {:x}".format(format_value_six))