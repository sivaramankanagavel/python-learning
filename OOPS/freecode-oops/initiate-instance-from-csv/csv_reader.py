import csv

"""
Here we are doing the automatically created the instance based on the csv data file.
1. we read the data from the csv file (without space we have ot provide the data in csv) using the csv package
   using csv package and utilize the DictReader() method to read the csv file and initiate the class into
   object.
2. Main concept here how it's possible to create the object without assign the class name into the variable.
   it's done by @classmethod this will help you to initiate the class into object without explicitly creating it.
"""


class Items:
    # class level variable:
    instance_created = []

    def __init__(self, name: str, price: float, quantity: float):
        # assert validation:
        assert price >= 0, f"the Price {price} value is not greater than or equal to zero"
        assert quantity >= 0, f"the Quantity {quantity} value is not greater than or equal to zero"

        # Instance variable assignment:
        self.name = name
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

    def __repr__(self):
        return f"Items('{self.name}', {self.price}, {self.quantity})"


Items.instance_created_auto()
print(Items.instance_created)
print(Items.num_is_integer(4))