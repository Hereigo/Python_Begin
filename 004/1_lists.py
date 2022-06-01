# =========== LISTS : ===========
list = ['aaa', 111, 22.33, True, None]
# list.sort() - TypeError: '<' not supported between instances of 'int'

# SLICE - [FROM : TILL : STEP] :
backward = list[::-1]
print(backward)  # [None, True, 22.33, 111, 'aaa']

# =========== LIST of FUNCs : ===========
f_list = [print, len]
a_list = ['aaa', 'ssss', 'dddddd']

for f in f_list:
    for a in a_list:
        if f.__name__ == 'print':
            f(a)
        else:
            print(f(a))

# NO OUT-OF-RANGE-EXCEPTION! :
print(a_list[2:10])  # 'dddddd'

# CLONE list by SLICE :
new_list = a_list[:]  # from first to last
string1 = 'qazxswedcvfr'
string2 = string1[:]

print(new_list is a_list)  # False - EQUAL but DEFFERENT VALUES.
print(string1 is string2)  # True - CLONED STRING created by REFERENCE!

print('aaa' in a_list)  # True - CONTAINS IN LIST!
print('aayy' < 'ab')  # True - ABC SORT.

print(max(a_list))  # 'ssss' - MAX in LIST

# LIST MANIPULATION :
a_list += ['xxx', 'yyyy']  # LIST ADD.
print(a_list)  # ['aaa', 'ssss', 'dddddd', 'xxx', 'yyyy']

del a_list[-3]  # LIST REMOVE.
print(a_list)  # ['aaa', 'ssss', 'xxx', 'yyyy']

a_list[1:3] = ['new', 'fffff']  # LIST INSERT.
print(a_list)  # ['aaa', 'new', 'fffff', 'yyyy']

a_list += 'abc'  # LIST CONCAT STRING.
print(a_list)  # ['aaa', 'new', 'fffff', 'yyyy', 'a', 'b', 'c']

# LIST Empty is BOOL()==FALSE
print(bool([]))     # False
print(bool([None]))  # True!
