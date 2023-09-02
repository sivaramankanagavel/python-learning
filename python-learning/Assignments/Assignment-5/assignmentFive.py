"""
Here we are going to read, write and append the data on the text file exercise.
"""
read_value = ""
new_write_value = ""

with open("test_text.txt", 'r') as textFile:
    read_value = textFile.read()

print(read_value)

new_write_value = read_value.replace('ducks', 'cows')

with open("test_text.txt", 'w') as textFile:
    textFile.write(new_write_value)

with open("test_text.txt", 'r') as textFile:
    read_value = textFile.read()

print(read_value)