"""
while loop and for loop
"""

numbers = [23, 27, 44, 56]
fruits = ["Apple", "mango", "strawberry"]
name = "Sivaraman K"

# --- while loop ---#
num = 0
while num < len(numbers):
    print(numbers[num])
    num += 1

while num < len(fruits):
    print(fruits[num])
    num += 1

# --- for loop ---#
for fruit in fruits:
    print(fruit)

for nameWord in name:
    print(nameWord)

for num in range(0, len(numbers)):
    print(numbers[num])