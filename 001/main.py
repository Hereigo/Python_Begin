# Function definition:
def my_print(name):
    print(f'My name is "{name}" because I am Started Module!)')


if __name__ == '__main__':
    my_print(__name__)

# MULTI-Line text by Triple Quottes:
myMultilineStr = '''Aaaaaaaaaaaa

Bbbbbbbbbbbb       BBBBBB 
        Cccccccccc   ...'''
print(myMultilineStr)
print(myMultilineStr.lower().splitlines())  # SPLIT by LINES
print(myMultilineStr.upper().split())  # SPLIT by WORDS

# FORMATTED String:
a = 4
b = 3
print('Example-1: %d - %d = %d' % (a, b, a - b))
print('Example-2: {} + {} = {}'.format(a, b, a + b))
print(f'Example-3: {a} - {b} = {a - b}')

# RAW String:
print(r"RAW Text: Blablabla \ aaa \r\n bbb")
# Symbols SCREENING:
print("SCREENING: Blablabla \\ aaa \\r\\n bbb")

# Strings MULTIPLICATION:
print('Abc.' * 10)

myStr = 'Abcdefghijk'

# If STRING contains SUB-STRING:
print('cde' in myStr)  # => True

# LAST CHAR in STRING (Counts from the END):
print(myStr[-1])  # k

# String [ FROM : TO : STEP ]
print(myStr[3:10:2])  # dfhj

# STRING as BOOL:
print(bool(''))  # FALSE

# String OUT with SEPARATORS:
print('aaa', 'bbb', 'ccc', 'ddd', sep=';  ')

# Strings with END:
print('abc', end='\n\n')  # double ENTER
print('he', end='')  # with NO END of line
print('llo')
