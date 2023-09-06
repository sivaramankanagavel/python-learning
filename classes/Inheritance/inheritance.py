"""
Creating the class and methods

Here the self in every method was referring the current object which one accessing this class in other
language we called as constructor here we called __init__(self).

and the __init__(self) have some variable that all are called instance variable because
those are all under methods.

one initializer and two methods we have in this class.

and you have to access the class variable using class name and dot operator to access it,
but in instance variable you have to access through the object name and dot operator.
"""


# Creating Class :

class User:  # super class or parent class or base clas
    no_of_users = 0  # class variable

    def __init__(self, user_name, password):
        self.user_name = user_name  # instance variable
        self.password = password
        User.no_of_users += 1

    def print_the_user_name(self):
        print("The {} was logged in...".format(self.user_name))

    def print_password(self):
        print("The password is {}".format(self.password))


# Inheritance ex-1:
class Student(User):  # derived class or child class

    def print_student_details(self):
        print("Hello Student " + self.user_name)


# Inheritance ex-2:
class Teacher(User):

    def __init__(self, age, subject, user_name, password):
        super().__init__(user_name, password)
        self.age = age
        self.subject = subject

    def print_teacher_details(self):
        print("Hello teacher " + self.user_name)
        print("Teacher tutoring this {} subject and his age is {}".format(self.subject, self.age))


"""
Multiple and Multi-level Inheritance:

multiple: if want to get too many methods from different parent or super or base class this is called 
          multiple inheritance.

multi-level: multi-level inheritance means we have to declare the child class as parent for another
             child class is multi-level inheritance.
"""


# multi-level Inheritance:
class MultiLevel(Teacher):
    def print_multilevel_details(self):
        print("Multi Level Inheritance user name: " + self.user_name)
        print("Multi Level Inheritance age: " + self.age)


# Multiple Inheritance:
class MultipleInherit(Student, Teacher):
    def print_multiple_inheritance(self):
        print("Teacher Inheritance: " + self.subject)
        print("Student Inheritance: " + self.user_name)
