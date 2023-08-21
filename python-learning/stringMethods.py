"""
Here I am going to try all main methods in String data type

"""

name = "Sivaraman"
name1 = "siva raman"
dob = "16/04/1996"
age = 27

print("Hi my name is " + name +
      " and my date of birth is " + dob +
      " and your age based on dob is " + str(age)
      )
print("upper case conversion -->", name.upper())
print("lower case conversion -->", name.lower())
print("length of the given string value -->", len(name))
print("type of the given data -->", type(name))
print("find the given char in the string -->", name.find("r"))
print("converts the first letter of the each word in capital letter  -->", name1.title())
print("convert the first letter in capital -->", name.capitalize())
print("replacing the existing word with new word, new word is second argument -->",
      name.replace("a", "o"))

# str.capitalize() method
"""
here we converting the foirst letter of the given string into capital
"""
print(name1.capitalize())

# str.casefold() method
""" 
str.casefold() method is used to convert every char into lower case and seems like str.lower() but here 
it's doing more than lower() method like it's converting some language styled format styles into normal text.
"""
print(name1.casefold())

# str.center() method
""" 
here we center the given text based on the given space value to this method.
the passed space value is equal to the given string means it return the same value. 
"""
print(name.center(15, ":"))

# str.count() method
"""
Here we are counting the passing string value was occured on the main string how many time.
"""
count1 = "hello world"
count2 = "o"
print(count1.count(count2))

# str.encode('utf-8')
"""
Here we are encode as well decode the different languages into standard utf-8 format
"""
text = "Hello, 世界!"
print(text.encode(encoding='utf-8'))

# str.endswith() method
"""
endswith() method check the passing string value was ended in the given main string value if it there 
it return the true value otherwise false value.
"""
text_one = "Hello world"
print(text_one.endswith("d"))
print(text_one.endswith("e"))

# str.expandtabs() method
"""
the expandtabs method was gives the space between based on the passing tabs spacing number value
"""
text_two = "hello\tworld"
print(text_two.expandtabs(tabsize=8))

# str.find() method
"""
If you want to find particular character in the given string use find method.
it always return the first appeared char index value.
"""
print(text_one.find("o"))

# str.format() method
"""
this method is used to place some values dynamically in the string format we already declare some values as 
placeholder in the string.
"""
text_three = "My name is {name} and I am working as a {profession} at {company_name}"
print(text_three.format(name="Sivaraman", profession="React Developer", company_name="NTT Data"))

# str.format_map() method
"""
here we passing the object as the parameter to the method and it will automatically assign the given placeholder 
name value from the given object. 
"""
data = {
      "name": "Sivaraman",
      "profession": "React Developer",
      "company_name": "NTT Data",
      "work_location": "Bangalore"
}
text_four = "Hi myself {name} and my profession is {profession}, I am working in {company_name} at {work_location}"
print(text_four.format_map(data))

# str.index() method
"""
if you want to find the index of the given char on the main string you can use this index method
"""
text_five = "Hello world"
print(text_five.index("w"))

# str.isalnum() method
"""
if the passing string values all are alphanumeric it return true or else return false
"""
text_six = "hi12345 6789"
text_seven = "123456789"
text_eight = "hi1234"
print(text_six.isalnum())
print(text_seven.isalnum())
print(text_eight.isalnum())

#-------------------------#

# str.join() method
"""
you have to join the set of string values into single piece of word
"""

#example-1
words = ["Hello", "world", "how", "are", "you?"]
separator = " "
print(separator.join(words))

#example-2
words = ["hello", "world", "how", "are", "you"]
empty_separator = ""
print(empty_separator.join(words))

#example-3
text = "Python is awesome!"
separator = "-"

result = separator.join(text)
print(result)

#example-4
multi_line_text = """This is a multi-line
string in Python.
We can join these lines."""

lines = multi_line_text.splitlines()
separator = " "

result = separator.join(lines)
print(result)

# -------------------- #