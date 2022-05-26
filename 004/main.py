print(' =========== LISTS : =========== ')
list = ['aaa', 111, 22.33, True, None]

# SLICE - [FROM : TILL : STEP] :
backward = list[::-1]
print(backward)  # [None, True, 22.33, 111, 'aaa']

print(' =========== LIST of FUNCs : =========== ')
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

