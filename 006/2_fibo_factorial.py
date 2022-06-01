def fib(n):
    if n == 1 or n == 2:
        print('n', n, '- x', 0)
        return 1
    else:
        x = fib(n - 1) + fib(n - 2)
        print('n', n, '- x', x)
        return x


# n 2 - x 0
# n 1 - x 0
# n 3 - x 2
# n 2 - x 0
# n 4 - x 3
# n 2 - x 0
# n 1 - x 0
# n 3 - x 2
# n 5 - x 5
# Fibonacci: 5
print('Fibonacci:', fib(5))
print('----------------------------')


def factorial(n):
    if n == 0:
        print('n', n, '- x', 0)
        return 1
    else:
        x = n * factorial(n - 1)
        print('n', n, '- x', x)
        return x


# n 0 - x 0
# n 1 - x 1
# n 2 - x 2
# n 3 - x 6
# n 4 - x 24
# n 5 - x 120
# Factorial: 120
print('Factorial:', factorial(5))
