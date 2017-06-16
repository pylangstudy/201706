global_var = 'global_var'
def func():
#    nonlocal global_var # SyntaxError: no binding for nonlocal 'global_var' found
    global_var = 'global_var_local_use'
#    nonlocal global_var # SyntaxError: name 'global_var' is assigned to before nonlocal declaration
    print(global_var)
#    nonlocal global_var # SyntaxError: name 'global_var' is used prior to nonlocal declaration
    print(global_var)
    
func()
