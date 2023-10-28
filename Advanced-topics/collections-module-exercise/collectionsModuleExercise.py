from collections import Counter, OrderedDict, defaultdict, deque, ChainMap, namedtuple
"""
Collection is a Module it will provide some methods to perform certain operations like,
1. Counter --> used to count the no of occurrence of the sequence.
2. namedtuple --> used to initialize the class with default arguments
3. OrderDict --> it will maintain the order of the dict key's certain manner.
4. defaultdict --> it will give the default value as 0 when the given key not present in the dict.
5. deque --> you can able to add, remove on both sides of the list.
6. ChainMap --> it was used to combine two dict into single dict.
"""

# Counter
list_one = [1, 2, 3, 4, 2, 3, 1, 3, 2, 2, 4, 5]
string_one = "Hello World !"
counter_one = Counter(string_one)
counter_two = Counter(list_one)

print(counter_one)
print(counter_two)

# defaultdict
dict_one = defaultdict(int)
dict_one["a"] = 20

print(dict_one)
print(dict_one["b"])

dict_two = defaultdict(str)
dict_two["name"] = "Sivaraman"
print(dict_two["age"])

# OrderDict
order_dict = OrderedDict()
order_dict["one"] = 1
order_dict["two"] = 2
order_dict["three"] = 3

printing_values = [order_dict[key] for key, value in order_dict.items()]
print(printing_values)

# deque
list_three = [20, 25, 40, 44, 77, 88]
deque_one = deque(list_three)
deque_one.append(100)
deque_one.appendleft(121)
print(deque_one)
deque_one.pop()
deque_one.popleft()
print(deque_one)

# namedtuple
Greetings = namedtuple("Greetings", ["name", "age"])
greet_one = Greetings("Sivaraman", "27")
print(greet_one)

# ChainMap
dict_three = {"a": 1, "b": 4}
dict_four = {"c": 3, "d": 5}

chain_map = ChainMap(dict_three, dict_four)
print(chain_map)
print(chain_map["c"])