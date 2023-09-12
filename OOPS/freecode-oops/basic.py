class Item:

    """
    This class level variable we are not able to access even inside of the same class so, if you want to
    access using the class name or (self) method to access the class level variables.
    """
    interest_rate = 0.3  # class level variable
    instance_created_list = []

    def __init__(self, name: str, price: float, quantity: float):
        # Parameter validation:
        assert price >= 0, f"The Price {price} was not greater than or equal to zero."
        assert quantity >= 0, f"The quantity {quantity} was not greater than or equal to zero."

        # Assigning parameter to the instance variable:
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append the instance values to the class level variable:
        Item.instance_created_list.append(self)

    def total_price(self):
        return self.price * self.quantity

    def discount_price(self):
        self.price = self.price - self.price * self.interest_rate

    """
    Representation Method __repr__() to represent the Object in your own way.It will automatically called on each
    instance created.
    """
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


item1 = Item("Sony Television", 25500, 3)
item2 = Item("Dell Laptop", 72000, 1)
item3 = Item("Water Heater", 15500, 2)
item4 = Item("VOLTAS AC", 32500, 3)
item5 = Item("IBF Washing Machine", 35500, 1)


print(item1.total_price())

# Want to know the attributes at the class as well as for the Instance level:
print(Item.__dict__)  # class level
print(item1.__dict__)  # Instance level

print(Item.interest_rate)
item1.discount_price()
print(item1.price)

# Representing the Object instance created we get them here:
print(Item.instance_created_list)
