spam = "global(module)"
def scope_test():
    def do_local():
        spam = "local"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal"

    def do_global():
        global spam
        spam = "global"

    spam = "test"
    do_local()
    print("In middle scope local:", spam)
    do_nonlocal()
    print("In middle scope nonlocal:", spam)
    do_global()
    print("In middle scope global:", spam)

print("In global scope before:", spam)
scope_test()
print("In global scope after:", spam)


