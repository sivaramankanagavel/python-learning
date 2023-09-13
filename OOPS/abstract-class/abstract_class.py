from abc import ABC, abstractmethod

"""
1. Abstract class is nothing but a class which one not instantiated directly from 
   outside of the class or either in the same class.

2. If you want to instantiate the abstract class, you done it through the child class with the exact abstract method.

3. if you try to instantiate the child class without abstract class method it throws Error.
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.24 * self.radius

