from classes.method_overriding.method_overridding import *

"""
Method overriding Exercise:
"""

user_one = User("Sivaraman", "siva123")

student_one = Student("Venkatesh", "thermo dynamics")

teacher_one = Teacher("Jothiram", "Petro chemical")


print(user_one.print_user_details())
print(student_one.print_user_details())
print(teacher_one.print_user_details())

# method chaining:
print(teacher_one.print_user_details().greet())