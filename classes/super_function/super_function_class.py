"""
super() function will help you to initialize the parent variable from the child.
1. In java they don't allow the multiple inheritance due to some issue, like if you have more than one parent at
   the time if you invoke the super() method i will cause the confusion to which parent class to initialize.
2. But in Python you have to do the multiple inheritance due to here the python will check the super() function
   in first parent and then next parent it goes up like that, if the specified method it will found at first
   parent class it will invoke that or else as previously mentioned like it will goes next parent to check
   this method is existing or not.

   # A.__init__(self, a_value)
   # super().__init__(a_value, b_value)
   # super(B, self).__init__(a_value, c_value)
   # super(C, self).__init__(a_value, c_value)
"""


class A:

    def __init__(self, a_value):
        self.a = a_value

    def print_value(self):
        print("A Value: " + self.a)


class B(A):

    def __init__(self, a_value, b_value):
        A.__init__(self, a_value)
        self.b = b_value

    def print_value(self):
        print("B Value: " + self.b)


class C(A):

    def __init__(self, a_value, c_value):
        A.__init__(self, a_value)
        self.c = c_value

    def print_value(self):
        print("C Value: " + self.c)


class D(B, C):

    def __init__(self, a_value, b_value, c_value, d_value):
        super().__init__(a_value, b_value)
        super().__init__(a_value, c_value)
        self.d = d_value

    def print_value(self):
        print("D values: " + self.d)