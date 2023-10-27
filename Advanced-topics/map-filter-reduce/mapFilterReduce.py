from functools import reduce
"""
Map --> Map is using to iterate each element from the List, here you have to pass the first parameter as
        function which is used to what we are going to do with iterable item from the map and second
        parameter as which List you want to iterate, map(function, []).
"""
# Question 1:
list_map_1 = [("Maths", "Anitha", 180), ("Biology", "Anand", 182), ("Biology", "Balaji", 170), ("Maths", "Chandru", 190)]

# Question 2:
list_map_2 = [72, 79, 99, 12, 56]

# Question 3:
list_map_3 = [102, 99, 89, 70, 103]

# Ans 1:
answer_one = list(map(lambda item: (item[1], item[2] / 2), list_map_1))

# Ans 2:
answer_two = list(map(lambda item: "Even" if item % 2 == 0 else "Odd", list_map_2))

# Ans 3:
answer_three = list(map(lambda item: float("{:.2f}".format((item - 32) * (5/9))), list_map_3))

print(answer_one)
print(answer_two)
print(answer_three)

"""
Filter ---> In filter function we need to pass the function as first parameter and 
            this function have some condition if it satisfied then it will return the
            data or else return nothing.
"""

filter_result = list(filter(lambda x: x % 2 == 0, list_map_3))
print(filter_result)

"""
Reduce ---> In reduce function we need to pass the first parameter as a function here 
            we have two arguments received and we process the two arguments and return
            new list with single data.
"""

reduce_result = reduce(lambda x, y: x+y, list_map_3)
print(reduce_result)