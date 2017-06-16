global_var = 'global_var'
def func():
    print(global_var)
    global global_var # SyntaxError: name 'global_var' is used prior to global declaration
    
func()
