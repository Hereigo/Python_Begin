list = ['aaa', 111, 22.33, True, None]

for i in list:
    print(i)

print(' === LIST of FUNCs : === ')
f_list = [print, len]
a_list = ['aaa', 'ssss', 'dddddd']

for f in f_list:
    for a in a_list:
        if f.__name__ == 'print':
            f(a)
        else:
            print(f(a))
