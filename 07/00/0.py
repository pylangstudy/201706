def Cond1():
    print('Cond1')
    return True
def Cond2():
    print('Cond2')
    return True
    
print('----- or -----')
if Cond1() or Cond2():
    print('Finished!!')
print('----- and -----')
if Cond1() and Cond2():
    print('Finished!!')
