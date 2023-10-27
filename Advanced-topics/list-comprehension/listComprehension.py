"""
List Comprehension --> Here we are using some shot hand techniques to to the new filter operation with out using
                       the filter keyword
                       1. [expr for item in iterable]
                       2. [expr for item in iterable if condition]
                       3. [expr if-else condition for item in iterable]
"""

list_one = [1, 2, 3, 4, 5, 6, 7, 8]

print([x**2 for x in range(1, 11)])
print([x for x in range(1, 11) if x % 2 == 0])
print([x**2 if x % 2 == 0 else None for x in range(1, 11)])