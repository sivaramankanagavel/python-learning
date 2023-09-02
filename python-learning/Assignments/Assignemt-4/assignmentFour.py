"""
Implement the sorting of the array without using the default sort method.
"""
sort_array = [56, 54, 49, 50, 47]
highest_number = 0
new_sort_array = []

for num in sort_array:
    if highest_number < num:
        highest_number = num
    else:
        continue

for num in range(0, highest_number + 1):
    if num in sort_array:
        new_sort_array.append(num)
    else:
        continue

print(new_sort_array)