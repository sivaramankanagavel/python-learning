from items import *
from phone import *

item1 = Items("Voltas", 35000, 3)
phone1 = Phone("Sivaraman", 45000, 1, "iphone 11 pro")

print(phone1.increment_price(5000))
print(phone1.increase_the_quantity(3))
print(phone1)
print(phone1.ph_name)

