"""
Here we are going to print some pattern of star and number in some format using for or while Loops.
"""

"""
Question 1:
            *
            **
            ***
            ****
            *****
"""

for i in range(1, 7):
    for j in range(1, i):
        print("*", end="")
    print("")

"""
Question 2: 
             *
            ***
           *****
          *******
"""

for i in range(1, 6):
    for j in range(6 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print(" ")

"""
Question 3:
            *******
             *****
              ***
               *
"""
for i in range(5):
    for j in range(i + 1):
        print(" ", end="")
    for k in range(1, 10 - (i + i)):
        print("*", end="")
    print()
