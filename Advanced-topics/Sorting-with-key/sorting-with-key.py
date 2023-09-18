"""
Sorting the list of tuple with sort() method is using the first element to sorting it, but
if you want to sort the list of tuple or list of dict with your preferred key is know as
sorting with key.
"""

list_tuple_values = [(123, "Hello", True), (345, "world", False), (234, "python", True)]
list_dict_values = [{"name": "siva", "age": 27}, {"name": "venki", "age": 25},
                    {"name": "Jothiram", "age": 27}]
tuple_of_tuple = ((4, "Samsung", 25000), (3, "Apple", 45000), (6, "Nokia", 15000))
dict_of_dict = {"item1": {"name": "siva", "age": 27}, "item2": {"name": "venki", "age": 25},
                "item3": {"name": "Jothiram", "age": 27}}

list_tuple_values.sort(key=lambda item: item[1])
print(list_tuple_values)
list_dict_values.sort(key=lambda item: item["name"], reverse=True)
print(list_dict_values)
print(sorted(tuple_of_tuple, key=lambda item: item[1]))
print(sorted(dict_of_dict.items(), key=lambda item: item[1]["name"]))
