import struct
with open('some.bin', 'wb') as f:
    for x in [0xFF, 0x12, 0x89]:
        f.write(struct.pack("B", x))
    f.write(bytearray([0xFF, 0x12, 0x89]))
with open('some.bin', 'rb') as f:
    print(f.read())

