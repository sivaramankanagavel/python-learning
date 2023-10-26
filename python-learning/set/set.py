"""
set this is used to store the data like dictionary but without key value.

and it will return the unique values and remove the duplicated values as well as the non-ordered.

you can convert the set into tuples and list.
"""

# Set exercise:

set_value = {"Dubai", "Qatar", "Saudi", "USA"}
print(set(set_value))

# converting the set into tuple and list:

print(list(set_value))
print(tuple(set_value))

set_one = {1, 2, 3, 4, 10, 11, 12}
set_two = {1, 2, 3, 5, 6, 7, 8}

# difference, update, symmetrical difference, symmetrical update, intersection difference update
"""
update method doesn't return the new set once it's update we need to print
in the next line to see the updated one. 
but remaining method return the new set value.
"""
# difference_one = set_one - set_two
# difference_two = set_one.difference(set_two)
#
# print(difference_one, difference_two)

# set_one.update(set_two)
# print(set_one)

# difference_three = set_one.symmetric_difference(set_two)
# print(difference_three)

# set_one.symmetric_difference_update(set_two)
# print(set_one)

# print(set_one.intersection(set_two))

# set_one.intersection_update(set_two)
# print(set_one)

set_three = {1, 2, 3, 4, 5}
set_four = {1, 2, 3}
# union, issubset, issuperset:
"""
issubset --> we are checking the first set all values present in the second set
issuperset --> we are checking the second set all values present in the first set
               reversible process of the issubset.

isdisjoint --> here we are checking the two set's doesn't have the common elements if 
               it's have then it return False otherwise True.
"""
# print(set_one.union(set_two))
print(set_three.issubset(set_four))
print(set_four.issubset(set_three))

print(set_three.issuperset(set_four))
print(set_four.issuperset(set_three))

set_five = {1, 2, 3}
set_six = {4, 5, 6}
set_seven = {3, 5, 6}

print(set_five.isdisjoint(set_six))
print(set_five.isdisjoint(set_seven))