"""
Assignemnt -2:

1. str_ip = "34, 5, 6, 7, 9" given a string of numbers and comma, add the numbers and deliminate the comma's.
"""

# Question - 1:
str_ip = "34,4,5,7,8"
total = 0

for i in str_ip:
    if i == ",":
        continue
    total += int(i)

print(total)