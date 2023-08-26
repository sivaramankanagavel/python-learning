"""
There are Eight different data types in python let see on by one
1. Text type
2. Numeric types
3. Sequence types
4. Mapping types
5. Set types
6. Boolean type
7. Binary types
8. None type
"""

# ---- Text Type ---#
"""string (str)"""
value_str = "Hai Python"
print(type(value_str))

# ---- Numeric Type ---#
"""Int (int)"""
value_int = 10

"""float"""
value_float = 10.56

"""complex"""
z1_complex = 3 + 4j
z2_complex = 3 - 5j
print("Imaginary Number" + str(z1_complex.imag))
print("Real Number" + str(z1_complex.real))
print(z1_complex + z2_complex)

# ---- Sequence Type ---#
"""list"""
value_list = ["grapes", "mango", "apple"]

"""tuple"""
value_tuple = ("ISRO", "NASA")

"""range(start, stop, step)"""
value_range = range(1, 10)
num_list = list(value_range)
print(num_list)

value_range_one = range(20, 30, 3)
num_list_one = list(value_range_one)
print(num_list_one)

# ---- Mapping Type ---#
"""mapping data type"""
value_mapping = {"name": "sivaraman",
                 "occupation": "React-Developer",
                 "education": "B.E(EEE)",
                 "yearOfPassout": 2018
                 }
print(value_mapping.values())
print(value_mapping.keys())
print(value_mapping.items())
for key, value in value_mapping.items():
    print(key, ":", value)

#---- Set Types ---#

"""set data type is mutable and you do the some operation"""
value_set = {
    "Grapes",
    "Banana",
    "Mango",
    "cucumber"
}

for item in value_set:
    print(item)

value_set.add("Strawberry")
print(value_set)
value_set.discard("Banana")
print(value_set)
value_set.remove("cucumber")
print(value_set)

"""
frozen data type are Immutable you can't add or update or 
delete the data from the object set
"""
value_frozen_type = frozenset({
    "mango",
    "pineapple",
    "strawberry"
})

print(value_frozen_type)

#---- Boolean ---#
value_boolean = 0
value_boolean_one = 1
value_boolean_true = True
value_boolean_false = False

#---- Binary Types ---#
value_binary = bytes(10)
value_binary_array = bytearray([45, 60, 55, 77])
value_binary_memory_view = memoryview(bytes(5))

print(value_binary)
print(value_binary_array)
print(value_binary_memory_view)

#---- None Type ---#
value_none = None
print(type(value_none))