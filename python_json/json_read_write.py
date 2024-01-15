import json

userDetails = {
    "name": "Sivaraman",
    "Age": 27,
    "profession": "Software"
}

with open("userJson.json", 'w') as json_write:
    json.dump(userDetails, json_write, indent=4)

with open("userJson.json", 'r') as json_read:
    readed_file = json.load(json_read)
    print(readed_file)