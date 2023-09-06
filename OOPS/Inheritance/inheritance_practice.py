from classes.Inheritance.inheritance import *

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