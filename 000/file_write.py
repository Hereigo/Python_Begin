import sys

# WRITE text (NOT APPEND!)
f = open('HELP_LIST.txt', 'w')
f.write('\n === SIMPLE TEXT AS TITLE === \n\n')
f.close()

# APPEND help() Command Output via Sys.StrOut
original_stdout = sys.stdout

with open('HELP_LIST.txt', 'a') as f2:
    sys.stdout = f2
    print(help('list'))
    sys.stdout = original_stdout
