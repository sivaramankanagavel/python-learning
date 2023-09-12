import csv

"""
Here we are going to doing the getter and setter function,
1. Getter --> the getter method was used to get the values from the class through using the
              @property decorator and it will return the class attributes.

2. Setter --> the setter function was used to set the values of the class attribute
              using the @<attribute name>.setter to define the function and return the 
              set value because here we are doing the encapsulation.

Using the getter and setter method to restrict the user to access the valuable data from outside the
class as well as once you initiate the class then you are not able to change the values directly
those are in read only state.

to make the variable in private as well as in read-only mode you can follow the below syntax:
1. readonly --> _<variable name>
2. private --> __<variable name>

then if you want to re-assign the value of the readonly you can use this @<variable name>.setter decorator
to to the assigning.   
"""


class Items:
    # class level variable:
    instance_created = []

    def __init__(self, name: str, price: float, quantity: float):
        # assert validation:
        assert price >= 0, f"the Price {price} value is not greater than or equal to zero"
        assert quantity >= 0, f"the Quantity {quantity} value is not greater than or equal to zero"

        # Instance variable assignment:
        self.__name = name
        self.price = price
        self.quantity = quantity

        # appending the list of instance created object into the class level variable:
        Items.instance_created.append(self)

    @classmethod
    def instance_created_auto(cls):
        with open("items.csv", "r") as csv_file_reader:
            reading_value = csv.DictReader(csv_file_reader)
            list_values = list(reading_value)

        for list_value in list_values:
            Items(
                name=list_value.get('name'),
                price=int(list_value.get('price')),
                quantity=float(list_value.get('quantity'))
            )

    @staticmethod
    def num_is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.__name = value

    def __repr__(self):
        return f"Items('{self.name}', {self.price}, {self.quantity})"