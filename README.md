# Python Begin.

#### STRINGS:
```py
multiLineByTripleQuot = '''Aaaa

Bbbb   bbbb
        Cccc   ...'''
multiLineByTripleQuot.splitlines()  # SPLIT by LINES
multiLineByTripleQuot.split()  # SPLIT by WORDS

# FORMATTING:
a,b = 3,4
print('1: %d and %d' % (a, b))
print('2: {} and {}'.format(a, b))
print(f'3: {a} and {b}')

# RAW String:
print(r"RAW Text: Blablabla \ aaa \r\n bbb")

# Symbols SCREENING:
print("SCREENING: Blablabla \\ aaa \\r\\n bbb")
```