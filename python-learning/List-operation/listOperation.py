"""
List Exercise.
it's a kind of Array.
"""

fruits = ["mango", "pineapple", "orange"]
numbers = [10, 15, 20, 25, 30, 35]

print(fruits[2])
print(numbers[2])

fruits[1] = "apple"
print(fruits)

# --- Append the data to List ---#
numbers.append(40)
print(numbers)

numbers.append(45)
print(numbers)

numbers.append(13)
print(numbers)

# --- Delete the data from the List ---#
del numbers[0]
print(numbers)

# --- Insert the data li the List on specific location ---#
numbers.insert(3, 27)
print(numbers)

# --- Remove the data from the List from last index ---#
print(numbers.pop())
print(fruits.pop())

# --- Remove the data from List ---#
fruits.remove("mango")
print(fruits)

# --- tempravory sorting of List ---#
print(sorted(numbers))
print(numbers)

#--- Permanent sorting in List ---#
numbers.sort()
print(numbers)