# DO it  IF  this-condition-is-True  ELSE  DO that!
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


# FOR IN (with STEP):
for i in range(-4, 4, 2):
    print(i)           #: -4, -2, 0, 2


# ITER() - for Iterables:
print(iter('123'), end='\n\n')
print(iter(123))  # TypeError: 'int' object is not iterable!


# LIST COMPREHENSION:
a = [x for x in range(5)]  # <class 'range'>
# same as
a = [0, 1, 2, 3, 4]

dict = {x: x+1 for x in range(4)}
# means
dict = {0: 1, 1: 2, 2: 3, 3: 4}


# NESTED LOOPS : #
width = 20
for i in range(0, width//2):
    for k in range(0, width+1):
        if (k >= width//2+i or k <= width//2-i):
            print(' ', end='')
        else:
            print('*', end='')
    print('')
#
#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************
