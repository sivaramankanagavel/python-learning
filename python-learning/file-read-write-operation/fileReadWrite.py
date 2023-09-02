"""
Here we are going to open the file which ever you want, here we are going to do the read and write
operation on the specified text file.
1. if you want to specify the mode of open the file on default state you can mention like
   'r' - read
   'w' - write
   'a' - append.
"""

write_value = "Hello Sivaraman writing was done"

with open("text.txt") as textFile:
    print(textFile.read())

with open("text.txt", 'a') as textFile:
    print(textFile.write(write_value))