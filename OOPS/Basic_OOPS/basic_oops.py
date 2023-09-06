"""
OOPS ---> Object Oriented Programming System, here we are making every action on every data for updating,
deleting and patching we do this operation as a class oriented.

for example: the user need to login so, we need to created a class called USER and in that we receive
             the attribute and we play with this attribute as methods inside the class.

             so, the attribute, methods all are wrapped by class.

             we creating this kind of class for every needs and we make every methods inside the class
             for particular purpose to play with the attributes.

             we converting this class into object then only you will able to play with this data.

second Example: Here you have to access the Class variables with class name and instance variable are
                accessed by Object name.

                and always stick with this approach because we are able to access the class variable with
                object name also but it was created the confusion so, we are avoiding this approach.
"""
from classes.basic_class.basic_class import *
# from classes.basic_class.basic_class import User
# from classes.basic_class.basic_class import Student
# from classes.basic_class.basic_class import Teacher

# Creating class and Object:

user1 = User("Sivaraman", "hello-python")
user2 = User("Venkatesh", "abc123")

user2.print_the_user_name()
user1.print_password()
print(User.no_of_users)

# Inheritance

student_one = Student("Siva", "abc789")
teacher_one = Teacher("45", "Science", "Ramesh", "Hello")

print(student_one.print_student_details())
print(teacher_one.print_teacher_details())

# multi-level inheritance:
multi_level_inheritance = MultiLevel("27", "Maths", "Raman", "Hello multi-level")
print(multi_level_inheritance.print_multilevel_details())

# multiple inheritance:
multiple_inheritance = MultipleInherit("27", "Social", "Jothi Ram", "jothi123")
print(multiple_inheritance.print_multiple_inheritance())