# FUNC PARAMS MUST BE <iterable>.

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


print(average([10, 15, 20, 100]))
# OR
print(average((10, 15, 20, 100)))
