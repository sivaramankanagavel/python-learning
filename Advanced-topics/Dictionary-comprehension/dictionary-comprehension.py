"""
Dictionary comprehension ---> Here also we doing some short-hand expression in dict data type
                              1. {key: expr for (key, value) in cart}
                              2. {key: expr for (key, value) in cart if condition}
                              3. {key: expr if-else condition for (key, value) in cart}
                              4. {key: function(key, value) for (key, value) in cart}
"""
cart = {"phone": 25000, "table": 10000, "chair": 6500, "lamb": 3500}

cart1 = {key: val for (key, val) in cart.items()}
print(cart1)

cart2 = {key: round(val * 0.9) for (key, val) in cart.items() if val > 10000}
print(cart2)

cart3 = {key: round(val * 0.85) if key == "phone" or "table" else val for (key, val) in cart.items()}
print(cart3)


def function_result(key, val):
    if key == "phone" or "table":
        val = round(val * 0.92)
        return val
    else:
        return val


cart4 = {key[0]: function_result(key, val) for (key, val) in cart.items()}
print(cart4)