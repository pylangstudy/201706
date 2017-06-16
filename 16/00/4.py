global_var = 'global_var'
def func():
    global global_var = 'global_var_local_use' # SyntaxError: invalid syntax
    print(global_var)
