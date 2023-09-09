"""
Method overriding is nothing but a we create a one method in a parent or super or base class,
In the same name we created another method in every child or sub class.

for example:
            1. The method called greet() we created in the parent class.
            2. and we created the same greet() method in the all child class.
            3. if you create the object for this child class and then invoke this greet() method.
            4. if you calling this method then python was looking this greet() method in the same class
               if it's there then it's overriding the parent greet() method.
            5. if it's not there then it's going forward to look the greet() method in parent... and then
               it invoking the greet() method.
"""


class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def print_user_details(self):
        print("Parent 1")
        print("Name : " + self.name)
        print("Password : " + self.password)


class Student(User):

    def __init__(self, student_name, fav_subject):
        super().__init__(name=student_name, password=fav_subject)

    def print_user_details(self):
        print("Child and Parent 1")
        print(User.print_user_details(self))


class Staff:

    def __init__(self, staff_name, staff_age):
        self.staff_name = staff_name
        self.staff_age = staff_age

    def print_user_details(self):
        print("Parent 2")
        print("Name : " + self.staff_name)
        print("Age : " + self.staff_age)


class Teacher(Student, Staff):

    def __init__(self, teacher_name, teacher_fav_subject):
        Student.__init__(self, teacher_name, teacher_fav_subject)
        Staff.__init__(self, staff_name=teacher_name, staff_age=teacher_fav_subject)

    def print_user_details(self):
        print("Last child")
        print(Student.print_user_details(self))
        print(Staff.print_user_details(self))
        return self

    def greet(self):
        print("Hello Teacher class")