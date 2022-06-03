def fibo_recur(n):
    global cnt
    cnt += 1
    if n in (1, 2):
        print('Counter:', cnt, '--- 1')
        return 1
    else:
        print('Counter:', cnt, '-', n)

    return fibo_recur(n-1)+fibo_recur(n-2)


cnt = 0
fibo_recur(5)
# Counter: 1 - 5
# Counter: 2 - 4
# Counter: 3 - 3
# Counter: 4 --- 1
# Counter: 5 --- 1
# Counter: 6 --- 1
# Counter: 7 - 3
# Counter: 8 --- 1
# Counter: 9 --- 1
#########################################################


def iter_from(obj, idx):
    return(obj[idx])


try:
    ob = 'abcd'
    ix = 3
    result = iter_from(ob, ix)
    err = ix/0
except IndexError:
    print(f'Error! - index [{ix}] > input last id [{(int(len(ob))-1)}]')
except Exception:
    print('"IndexError" not occured, but something else broken.(')
