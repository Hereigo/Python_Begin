def biggest_divider(x, y):
    result = 0
    divider = 2
    while divider < x and divider < y:
        if x % divider == 0 and y % divider == 0:
            result = divider
            print(result)
        divider += 1
    print('Result:', result)


x = 100  # input('Type first number:')
y = 20  # input('Type second number:')
biggest_divider(x, y)
