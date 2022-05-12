# Function definition:
def print_hi(name):
    print(f'Hi, {name}')


# MUST BE FIND OUT !
if __name__ == '__main__':
    print_hi('MegaPython!))')


# INPUT function returns STRING from Console INPUT:
insertedVarText = input('Enter your text to insert: ')
print(f"Some text with {insertedVarText}")


# String OUT with SEPARATORS:
print('aaa', 'bbb', 'ccc', 'ddd', sep='__Separator__')


# INPUT as FLOAT - NONE as Undefined:
result = None
x = float(input('Введіть перше число: '))
y = float(input('Введіть друге число: '))
result = x + y # Result will be FLOAT!
if result is not None:
    print(result)
