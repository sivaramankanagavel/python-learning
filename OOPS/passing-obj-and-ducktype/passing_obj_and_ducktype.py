"""
Passing a object and using that object method also in some outside methods is called duck-type passing
parameters.
"""


class Vehicle:
    def __init__(self, vehicle_name, year):
        self.__vehicle_name = vehicle_name
        self.__year = year

    def get_vehicle_name(self):
        return self.__vehicle_name

    def get_vehicle_year(self):
        return self.__year
