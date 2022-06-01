# MULTI-Line text by Triple Quottes:
multiLineByTripleQuot = '''Aaaa

Bbbb   bbbb
        Cccc   ...'''

print(multiLineByTripleQuot.splitlines())  # SPLIT by LINES
print(multiLineByTripleQuot.split())  # SPLIT by WORDS

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

myStr = 'Abcdefghijk'

# If STRING contains SUB-STRING:
print('cde' in myStr)  # => True

# LAST CHAR in STRING (Counts from the END):
print(myStr[-1])  # k

# String [ FROM : TO : STEP ]
print(myStr[3:10:2])  # dfhj

# String OUT with SEPARATORS:
print('aaa', 'bbb', 'ccc', 'ddd', sep=';  ')

# Strings with END:
print('abc', end='\n\n')  # double ENTER
print('he', end='')  # with NO END of line
print('llo')

# ID() :
a = 'Glory Of Ukraine !!!'
b = 'Glory Of Ukraine !!!'
print(a == b)  # True
print(a is b)  # True
print(id(a) == id(b))  # True
print(id(a) is id(b))  # False!!!
