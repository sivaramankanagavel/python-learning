from classes.super_function.super_function_class import *

class_d = D("Value A", "Value B", "Value C", "Value D")
class_d.print_value()
print(class_d.a)
print(class_d.b)
print(class_d.d)

# MRO (Method Resolution Order)
print(D.mro())