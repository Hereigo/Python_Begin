# Function definition:
def my_print(name):
    print(f'My name is "{name}" because I am Started Module!)')


if __name__ == '__main__':
    my_print(__name__)


# STRING as BOOL:
print(bool(''))  # FALSE

# FALSE or NONE:
print(False or None)  # NONE!

# INPUT data as FLOAT - NONE as Undefined:
result = None
result = float(input('Type number to Double it: '))
if result is not None:
    print(result * 2)
