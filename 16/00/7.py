module_var = 'global_var'
def func():
    func_var = 'func_var'
    def inner_func():
        print(func_var)
    inner_func()
    
func()
