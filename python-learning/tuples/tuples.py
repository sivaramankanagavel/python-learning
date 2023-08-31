"""
Tuple are similar to the list, but in the list we can add and remove the data from the list here we are
not going to add the data or remove the data from the tuple.

so tuple are immutable.
"""

# Tuple syntax:
tuple_value = (45, 65, 76)

# Tuple exercises:
print(tuple_value[1])
print(tuple_value.index(45))
print(tuple_value.count(45))

for tupleValue in tuple_value:
    print(tupleValue)

if tuple_value:
    print("Yes tuple contains some data")
