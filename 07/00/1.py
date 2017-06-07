def CondTrue():
    print('CondTrue')
    return True
def CondFalse():
    print('CondFalse')
    return False
    
print('----- True or False -----')
if CondTrue() or CondFalse():
    print('Finished!!')
print('----- False or True -----')
if CondFalse() or CondTrue():
    print('Finished!!')
