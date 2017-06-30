from array import array
ary = array('b', [-128, 127])
ary = array('B  ', [0, 255])
#ary = array('u', [u'ゆ', u'に'])    # 非推奨。Python4.0で削除予定。OverflowError: signed char is greater than maximum
# hとiは同じ2Byte
ary = array('h', [-32768, 32767])
ary = array('H', [0, 65535])
ary = array('i', [-2147483648, 2147483647])
ary = array('I', [0, 4294967295])
ary = array('l', [-2147483648, 2147483647])
ary = array('L', [0, 4294967295])
ary = array('q', [int(-(2**64)/2), int((2**64)/2)-1])
ary = array('Q', [0, (2**64)-1])
# 浮動少数点数 float, double
ary = array('f', [0.0])
ary = array('d', [0.0])

