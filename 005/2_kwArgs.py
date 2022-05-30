# FUNC PARAMS MUST BE <iterable>.
a_list = [10, 15, 20, 100]
a_tuple = (10, 15, 20, 100)


def average(list_or_tuple):
    total = 0
    for n in list_or_tuple:
        total += n
    return total / len(list_or_tuple)


print(average(a_list))
# OR
print(average(a_tuple))

# OR possible pass NON-ITERABLE!

# ARGS & KWARGS - MUST be **UNPACKED into Multiple Params


def average(*args):
    total = 0
    for n in args:
        total += n
    return total / len(args)


print(average(10, 15, 20, 100))

# Pass Tuple arise - TypeError: unsupported operand type(s) for +=: 'int'
# print(average(a_tuple)) - Error!
print(average(*a_tuple))  # Tuple MUST BE Expanded into MULTIPLE ARGS!

# KeyWord ARGuments - for NAMED Params OR DICTIONARIES
a_dict = {'aa': 11, 'bb': 22, 'cc': 33}


def kwa_test(**kwargs):
    for k, v in kwargs.items():
        print(k, '-key has value -', v)


kwa_test(**a_dict)
# OR Just Named Params
kwa_test(abc=123, bcd=234, cde=345)


def multi_params(a, b, *args, **kwargs):
    print('a = ', a)
    print('b = ', b)
    print('args = ', args)
    print('kwargs = ', kwargs)


# a =  aaa
# b =  222
# args =  (3, 4, 5)
# kwargs =  {'c': 11, 'd': 12, 'e': 14}
multi_params('aaa', 222, 3, 4, 5, c=11, d=12, e=14)
