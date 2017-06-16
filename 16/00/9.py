module_var = 'global_var'
def func():
    func_var = 'func_var'
    def inner_func():
        nonlocal func_var
        func_var = 'func_var_inner'
        print(func_var)
    inner_func()
    print(func_var)

func()
