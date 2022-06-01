# TUPLE - IMMUTABLE LIST :
# DICT-KEY Can be a TUPLE! but CAN'T be a LIST!

my_tuple = (1)

packed_as_tuple = 11, 22, 33, 44, 55
print(packed_as_tuple)  # (11, 22, 33, 44, 55)

item1, item2, item3, item4, item5 = packed_as_tuple
print(item3)  # 33

tuple2 = [(1, 2, 3), (4, 5, 6)]
for a, b, c in tuple2:
    print(a, b, c)

# DICT :
a_dict = {'first': 111, 'second': 22.22}

for i in a_dict:
    print(i)    # KEYS ONLY.

for i in a_dict.values():
    print(i)    # VALUES.

for i in a_dict.items():
    print(i)    # FULL ITEMS

print(a_dict.get('third', -1))  # Return Value IF Key Not Found.

# REVERSED RANGE:
for i in reversed(range(5)):
    print(i, end=', ')        # -> 4, 3, 2, 1, 0,
