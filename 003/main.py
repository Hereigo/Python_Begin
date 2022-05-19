
# Do it  IF  this-condition-is-True  ELSE  Do that!
print('Do it!') if 'Important' else print('Do nothing')

# TUPLES:
my_tuple = (0, 1, 2, 3, 4)

a, *b, c = my_tuple

print(b)  # [1, 2, 3]

# Operator PASS:
some_value = 'valid'

if some_value == 'valid':
    pass  # just Do Nothing
else:
    print('Value is Not Valid!')

# WHILE - ELSE :
x = 3
while x:
    x -= 1
    response = input('Type "stop" to stop: ')
    if response == 'stop':
        print('Loop Stopped!')
        break
else:
    print('Iteration just finished.')

# FOR IN :
for x in 'ABCD':
    print(x)

# ITER() - for Iterables:
print(iter('123'), end='\n\n')
print(iter(123))  # TypeError: 'int' object is not iterable!

