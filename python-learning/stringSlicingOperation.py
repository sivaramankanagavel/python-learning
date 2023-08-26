"""
String Slicing
H e l l o W o r l d.
0 1 2 3 4 5 6 7 8 9.¶
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1.
"""

name = "hello world"
print(name[2:4])

print(name[2:])
print(name[-3:-1])

print(name[-2:-5])

# --- choose the particular part in the string to print ---#
print(name[-5:-2])

# --- reverse the string ---#
print(name[::-1])

# --- printing the string in forward --#
print(name[::1])

# --- printing string in forward with two steps
print(name[::2])

# --- Slicing ---#
x = slice(2, -2)
print(name[x])