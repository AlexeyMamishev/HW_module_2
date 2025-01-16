def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = ['Moon', 2025, False]
values_dict = {'a':'sun', 'b':False, 'c':2013}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [911, 'day']
print_params(*values_list_2, 42)