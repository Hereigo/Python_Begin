import math  # імпротуємо модуль math

# Strings MULTIPLICATION:
print('Abc.' * 10)

# Calculatin Incomings of SubStrings:
lines = '''A
B b B
C c b
'''
print(sum('b' in line for line in lines.lower()))  # 4

######################################################

print(100 // 3)  # 33

print(100 % 3)  # 1

print(3 ** 3)  # 27
print(pow(3, 3))  # 27

x = 1.23456

print(round(x, 3))  # 1.235!
print(math.trunc(x))  # 1
print(math.floor(x))  # 1
print(math.ceil(x))  # 2

print(math.pi)
