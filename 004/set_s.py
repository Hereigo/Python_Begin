# SET - UNSORTED UNIQUE-VALUES COLLECTION.

s1 = set('aaabbbcccftgghjjk')
print(s1)  # {'c', 'g', 'b', 'k', 't', 'h', 'a', 'f', 'j'}

s2 = {'abc', 'xxx', 'fff', 'a'}
s3 = s1.union(s2)    # Unsorted!
# {'c', 'a', 't', 'abc', 'xxx', 'g', 'b', 'h', 'f', 'k', 'j', 'fff'}
print(s3)

print(s1.intersection(s2))   # {'a'}

print({1, 2, 3, 4}.difference({3, 4, 5, 6}))  # {1, 2}

print({1, 2, 3, 4}.symmetric_difference({3, 4, 5, 6}))  # {1, 2, 5, 6}

print({2, 3}.issubset({1, 2, 3, 4}))  # True

s4 = {1, 2, 3}
s4.discard(2)
print(s4)       # {1, 3}
s4.discard(2)   # nothing.
# s4.remove(2)  # KeyERROR!

