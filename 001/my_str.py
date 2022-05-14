# ID() :
a = 'Glory Of Ukraine !!!'
b = 'Glory Of Ukraine !!!'
print(a == b)  # True
print(a is b)  # True
print(id(a) == id(b))  # True
print(id(a) is id(b))  # False!!!


# Calculatin Incomings of SubStrings:
lines = '''A
B b B
C c b
'''
print(sum('b' in line for line in lines.lower()))  # 4


# INPUT data as FLOAT - NONE as Undefined:
result = None
result = float(input('Type number to Double it: '))
if result is not None:
    print(result * 2)
