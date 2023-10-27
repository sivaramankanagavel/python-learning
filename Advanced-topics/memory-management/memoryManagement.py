"""
Memory Management in Python:
 1. Here we having two memory location one is STACK and HEAP:
 2. stack always storing the variable name and HEAP always store the value of the variable.
 EX 1:
 1. a = 10
    b = 20
    c = 10
as per the above example the a and b values only created in HEAP memory but in STACK memory we have three
variable name of a, b, c here the b pointing out the 20 obj reference.
a and c was always pointing to the obj value 10.

so if you create the new variable value if that value was already having in the HEAP then it doesn't
create the new object value in the HEAP.

in STACK we have to set of memory one is for Main Execution variable and another one is Function variable.

EX 2:
a = 10
b = 20
c = 20

def test(x):
    x = 30

x = 40
test(x)
print(x)

1. when you execute this code the the STACK have the a, b, c and x in the main memory location.
2. and another one memory was created in the STACK called Function variable this one hold the value
   inside of the each function variable this memory was created for every single function separately
   in the function variable memory location.
3. here initially the x was pointing out the 40 from main variable and lately it was pointing to the 30 in
   the function memory location once this execution was completed, back to the main execution, at the time
   again this x was pointing the main memory value of the x.
4. so, the answer when you print the x value is 40 only even after assigning.
5. because the garbage collector in the python was always working based on the "reference count"
   when the reference count becomes "zero" at the time garbage collector was comes into the picture.
   and it will delete the variable value from the HEAP memory.
6. and it will erase the function memory once the function execution was completed.
7. Even every onj creation at the time pyton will create the new object in the HEAP memory.
"""

a = 10
b = 10
c = 20

print(id(a) == id(b))
print(id(a) == id(c))


def test(x):
    x = 30


x = 40
test(x)
print(x)

"""
In python why int, float, string, tuple are immutable means when ever you created the value on these
types, and try to reassign some values on this variable it always create the new value and new memory
location it doesn't erase the existing memory value and overwrite this will never happen.

so, this is the reason these data types are immutable in Python.
"""