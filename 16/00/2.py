global_var = 'global_var'
def func():
    global_var = 'global_var_local_use'
    print(global_var) # グローバル変数と同一のローカル変数があると、グローバル変数が参照できない

func()
