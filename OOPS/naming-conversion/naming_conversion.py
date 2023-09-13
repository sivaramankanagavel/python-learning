"""
1. If you running the any module directly --> In python we have the __name__ attribute it will return you are running
   directly or you running this module from some other place.

2. Running directly you getting this value in __name__ (__main__) otherwise you get the module name.
"""


class NameConversion:

    print(__name__)
    def __init__(self, value):
        self.value = value

    def print_name_value(self):
        return self.value
