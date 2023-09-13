from passing_obj_and_ducktype import *


def get_some_values(passed_value):
    return passed_value.get_vehicle_name()


car1 = Vehicle("Volvo", "2019")
print(get_some_values(car1))
