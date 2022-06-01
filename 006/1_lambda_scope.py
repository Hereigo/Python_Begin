############# LAMBDAS: #############
# labmda args: expression-with-return

# lmb = lambda a, b, c: a+b*c
from distutils.sysconfig import get_config_var


def lmb(a, b, c): return a+b*c


print(lmb(1, 2, 3))   # 7

########################################

lll = [
    lambda x: pow(x, 0),
    lambda x: pow(x, 1),
    lambda x: pow(x, 2),
    lambda x: pow(x, 3),
]

for lmb in lll:
    print(lmb(5))

############# L.E.G.B. #############

# 1_Local, 2_Enclosing, 3_Global, 4_Built-in - Scopes!

# See Accessible var & func in Current Scope.
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'lll', 'lmb']

print('len(dir(__builtins__)):', len(dir(__builtins__)))

############# GLOBAL (NONLOCAL) EXPLICIT #############


def func():
    outer_var = 'Outer Value'
    print(outer_var)

    def inner_func():
        # Use NONLOCAL 'outer_var' Here!
        nonlocal outer_var
        print(outer_var)
        outer_var = '- Outer Value modified inside inner_func'

        # Use GLOBAL 'g_var' Here!
        global g_var
        print(g_var)
        g_var = '- Global Value Modified inside Func()'

    inner_func()
    print(outer_var)


g_var = 'Global Value'
func()
print(g_var)  # 'New Local Value' - already here.
