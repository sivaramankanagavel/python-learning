from itertools import (product, permutations, combinations, combinations_with_replacement,
                       accumulate, groupby, count, cycle, repeat)
import operator
"""
iter-tools Module having certain methods this will perform certain operations
1. product --> it will take two list and it will return the possible combinations from the two list. (duplicate comb).
2. permutations --> it will take the single list and it return the possible combination (duplicate comb).
3. combinations --> it will take a single list and it will return the non-duplicate combinations.
4. combinations_with_replacement --> it will take single list and i make the combination with same value like(4,4)(5,5).
5. accumulate --> it takes single list and it will return new object with accumulated value like
                  [1, 2, 3] ===> result is [1, 3, 5], so it will accumulate the values based on the position
                  like first index return value it-self and second index return first + second value accumulation
                  likewise.
6. groupby --> this take a single list and it was return the object based on the given condition, the condition
               satisfied data in one group and non-satisfied data are in another group.
7. count --> this will start the count from 0 if you pass any int value in first argument it starts from that.
8. cycle --> it will continuously print some data you passed as an first argument upto the break condition execute.
9. repeat --> it will take first argument as data which you want print continuously and second argument is how many
              times you want to print or repeat this process that value you need to provide otherwise it will falls in
              infinite loop
              
              this count, cycle and repeat these are comes under infinite loop so be careful to handle it otherwise
              it will throw an stack overflow error.
"""

# product
list_one = [1, 2, 3]
list_two = [4, 5]
product_one = product(list_one, list_two)

print(list(product_one))

# permutation
list_three = [1, 2, 3]
permutation_one = permutations(list_three, 2)
print(list(permutation_one))

# combinations
list_four = [4, 5, 6]
combinations_one = combinations(list_four, 2)
print(list(combinations_one))

# combination with replacement
comb_replacement = combinations_with_replacement(list_four, 2)
print(list(comb_replacement))

# accumulate sum and multiplication
acc_list = [1, 2, 3, 4, 5]
list_accumulate_sum = accumulate(acc_list)
print(list(list_accumulate_sum))

list_multi = accumulate(acc_list, lambda x, y: x * y)
print(list(list_multi))

list_multi_two = accumulate(acc_list, func=operator.mul)
print(list(list_multi_two))

acc_list_two = [1, 2, 3, 4, 6, 5, 2]
list_multi_three = accumulate(acc_list_two, func=max)
print(list(list_multi_three))

# groupby
group_list = [1, 2, 3, 5, 7, 8, 9]
group = groupby(group_list, key=lambda x: x < 3)
print(list(group))
"""
it print like below
[(True, <itertools._grouper object at 0x000002336248F850>), (False, <itertools._grouper object at 0x000002336248F7C0>)]
"""
for key, value in group:
    print(key, list(value))

group_list_dict = [{"name": "Sivaraman", "age": 27}, {"name": "Jothiram", "age": 27}, {"name": "Vinoth", "age": 27},
                   {"name": "venkatesh", "age": 25}]

group_two = groupby(group_list_dict, lambda data: data["age"])

for key, value in group_two:
    print(key, list(value))
    """
    it will print like below format
    27 [{'name': 'Sivaraman', 'age': 27}, {'name': 'Jothiram', 'age': 27}, {'name': 'Vinoth', 'age': 27}]
    25 [{'name': 'venkatesh', 'age': 25}]
    """

# count, cycle, repeat
cycle_list = [1, 2, 3, 4]
count_value = count(5)
cycle_value = cycle(cycle_list)
repeat_value = repeat(44, 4)

for i in count_value:
    print(i)
    if i == 15:
        break

for i in cycle_value:
    print(i)
    break

for i in repeat_value:
    print(i)

