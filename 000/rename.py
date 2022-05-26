from os import walk
from os import listdir
from os.path import isfile, join
from posixpath import dirname

start_dir = '/home/aaa/Desktop/КВАРТИРА/КВАРТИРА/'

f = []
d = []
for(dirpath, dirname, filenames) in walk(start_dir):
    d.extend(dirname)
    f.extend(filenames)
    break

# for xpath in walk(start_dir):
#     f.extend(xpath)

for x in d:
    print(x)
