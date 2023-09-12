from items import *


class Phone(Items):

    def __init__(self, name: str, price: float, quantity: float, ph_name: str):
        super().__init__(name, price, quantity)
        self.__ph_name = ph_name

    @property
    def ph_name(self):
        return self.__ph_name

    @ph_name.setter
    def ph_name(self, value):
        self.__ph_name = value
