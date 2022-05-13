# Function definition:
def print_hi(name):
    print(f'My name is "{name}" because I am Started Module!)')


if __name__ == '__main__':
    print_hi(__name__)

# String OUT with SEPARATORS:
print('aaa', 'bbb', 'ccc', 'ddd', sep='__Separator__')

# MULTI-Line text by Triple Quottes:
print('''Aaaaaaaaaaaa

Bbbbbbbbbbbb       
        Cccccccccc''')

# FORMATTED String:
print(f"Some text with inserted text '{__name__}'")

# RAW String:
print(r"RAW Text: Blablabla \ aaa \r\n bbb")

# Strings MULTIPLICATION:
print('Abc.' * 5)

myStr = 'Abcdefghijk'

# If STRING contains SUB-STRING:
print('cde' in myStr)  # => True

# LAST CHAR in STRING (Counts from the END):
print(myStr[-1])  # k

# String [ FROM : TO : STEP ]
print(myStr[3:10:2])  # dfhj

# STRING as BOOL:
print(bool(''))  # FALSE

# INPUT data as FLOAT - NONE as Undefined:
result = None
x = float(input('Type first number: '))
y = float(input('Type second number: '))
result = x + y  # Result will be FLOAT!!!!!!
if result is not None:
    print(result)
