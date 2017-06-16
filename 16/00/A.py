module_var = 'global_var'
def func():
    func_var = 'func_var'

#print(func().func_var) # AttributeError: 'NoneType' object has no attribute 'func_var'
#print(func.func_var) # AttributeError: 'function' object has no attribute 'func_var'

