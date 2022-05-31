# SLASH / mark IN Params:
# - makes ALL params BEFORE as REQUIRED and ORDERED!
def a_func(a, b, /, z, x):
    ''' - This function do nothing.
 - Just demonstrating Slash mark using.
 '''
    pass


a_func('111', 222, x=444, z=333)
# a_func(b=222, z=333, x=444, a=111) - TypeError!
# a_func() got some positional-only arguments passed as keyword arguments: 'a, b'

# Functions Comments-DOCS:
print(a_func.__doc__)

# ANNOTATIONS:


def a_func(a: str, b: int, /, z: int, x: int) -> None:
    pass


print(a_func.__annotations__)

a_func(1, '222', '333')  # TypeError! by LINTER
