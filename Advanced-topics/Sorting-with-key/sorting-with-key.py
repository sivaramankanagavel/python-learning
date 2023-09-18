"""
Sorting the list of tuple with sort() method is using the first element to sorting it, but
if you want to sort the list of tuple or list of dict with your preferred key is know as
sorting with key.
"""

list_tuple_values = [(123, "Hello", True), (345, "world", False), (234, "python", True)]
list_dict_values = [{"name": "siva", "age": 27}, {"name": "venki", "age": 25},
                    {"name": "Jothiram", "age": 27}]

list_tuple_values.sort(key=lambda item: item[1])
print(list_tuple_values)
list_dict_values.sort(key=lambda item: item["name"])
print(list_dict_values)