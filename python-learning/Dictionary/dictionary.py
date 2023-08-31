"""
Dictionary is nothing but the Object we called in JavaScript.

Here you have to store the data as a key & value pair.
"""

# Dictionary:
dict_value = {
    "name": "Sivaraman",
    "Job": "React Developer",
    "Education": "B.E(EEE)"
}

# dictionary operations:
"""
1. you can able to get the key, value pair data using items() method.
2. only need a value means you should use the values().
3. key only means keys() method.
"""
for key, value in dict_value.items():
    print("Key: " + key + "Value: " + value)

for key in dict_value.keys():
    print("Keys: " + key)

for value in dict_value.values():
    print("Values: " + value)

"""
If you want you have to add or delete the data based on the key.
"""
dict_value["dob"] = "16/04/1996"
dict_value["year of passout"] = "2018"
print(dict_value)

del dict_value["year of passout"]
print(dict_value)

"""
Insert the dictionary into the tuple and Insert the tuple into dictionary as a value pair.
"""
user_data = [dict_value]
user_data[0]["location"] = "Bangalore"
print(user_data)

dict_value["favorite places"] = ["Bangalore", "Bhopal", "Rajasthan"]
print(dict_value)
