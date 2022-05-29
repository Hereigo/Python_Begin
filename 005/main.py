# FUNC SECOND CALL DO NOT USE DEFAULT PARAM IF VAL MODIFIED !!!

def default_param_func(my_list=[]):
    my_list.append('###')
    return my_list


print(default_param_func())  # ['###']
print(default_param_func())  # ['###', '###']
print(default_param_func())  # ['###', '###', '###']


# Also possible FUNC OVERRIDING
def default_param_func(my_list=[]):
    my_list.append('@@@')
    return my_list


print(default_param_func())  # ['@@@']
print(default_param_func())  # ['@@@', '@@@']
print(default_param_func())  # ['@@@', '@@@', '@@@']


def default_param_func(my_list=[]):
    return my_list


print(default_param_func())  # []
print(default_param_func())  # []
