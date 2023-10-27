"""
zip function was used to put together more than two iterable item in single tuple.
ex: 1
products = ["phone", "table", "chair", "lamp"]
prices = [7500, 5000, 2500, 500]
zip(products, prices) --> convert into list --> // [("phone": 7500), ("table": 5000), ("chair": 2500), ("lamp": 500)]
"""

products = ["phone", "table", "chair", "lamp"]
prices = [7500, 5000, 2500, 500]
stocks = [7, 5, 3, 10]
zipped_result = list(zip(products, prices, stocks))
print(zipped_result)