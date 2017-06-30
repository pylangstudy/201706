from array import array
ary = array('B', [0, 255, 127]) # B: unsigned char 0〜255(0x00〜0xFF) 
#ary = array('B', [0, 255, -1]) # OverflowError: unsigned byte integer is less than minimum
for a in ary: print(a)
print(sorted(ary))
