import json
import logging

# create custom logging for the creating JSON:
json_logger = logging.getLogger("JSON HANDLER")

# create handler for this logger:
file_handler = logging.FileHandler("JsonLogger.txt", 'w')

# set up the logger severity:
file_handler.setLevel(logging.ERROR)

# create format for this logger:
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                                   datefmt="%a-%d-%b-%y - %H:%M:%S")
file_handler.setFormatter(file_formatter)

# adding custom handler to the custom logger:
json_logger.addHandler(file_handler)

data = {
    "name": "Sivaraman",
    "age": 27,
    "favorite_places": ["Bhopal", "Maharashtra", "Bangalore"],
    "friends": [
        {
            "name": "Jothiram",
            "age": 27
        },
        {
            "name": "Vinoth kannan",
            "age": 27
        },
        {
            "name": "Blesson",
            "age": 27
        }
    ],
    "mobile_number": ("7598216496", "8903621198")
}

with open("write_json.txt", "w") as write_file:
    json.dump(data, write_file)

with open("write_json.txt", "w") as write_file:
    json.dump(data, write_file, indent=4)

with open("write_json.txt", "r") as read_file:
    json_data = json.load(read_file)
    print(data)


# custom serializer(encoder):
class CreateObject:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


class ErrorChecking:
    def __init__(self, name, age):
        self.name = name
        self.age = age


object_created = CreateObject("Siva", 27, "Kovilpatti")
error_checking = ErrorChecking("Jothiram", 27)


def custom_encoding(obj):
    if isinstance(obj, CreateObject):
        return {"name": obj.name, "age": obj.age, "city": obj.city}
    else:
        json_logger.error("wrong format of the object")


with open("write.json", "w") as writefile:
    json.dump(object_created, writefile, default=custom_encoding, indent=4)

with open("write_one.json", "w") as writefile:
    json.dump(error_checking, writefile, default=custom_encoding, indent=4)
