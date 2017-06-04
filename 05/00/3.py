a = {'A', 'B', 'C'}
b = {'D', 'E', 'A'}
print('a =', a)
print('b =', b)
print('a - b =', a - b) # 差
print('b - a =', b - a) # 差
print('a | b =', a | b) # 和
print('a & b =', a & b) # 積
print('a ^ b =', a ^ b) # 対称差
# a ^ b = (a | b) - (a & b)
print('(a | b) - (a & b) =', (a | b) - (a & b)) # 対称差

