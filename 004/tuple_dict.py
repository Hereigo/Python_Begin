# TUPLE - IMMUTABLE LIST :
# DICT Key Can be a TUPLE! but CAN'T be a LIST!

my_tuple = (1)
print(my_tuple)

packed = 11, 22, 33, 44, 55
print(packed)  # (11, 22, 33, 44, 55)
unpak1, unpak2, unpak3, unpak4, unpak5 = packed
print(unpak3)  # 33

# DICT :
a_dict = {'first': 111, 'second': 22.22}

for i in a_dict:
    print(i)    # KEYS ONLY.

for i in a_dict.values():
    print(i)    # VALUES.

for i in a_dict.items():
    print(i)    # FULL ITEMS
