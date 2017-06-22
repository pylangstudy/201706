import sys
#print(sys.stdin.read())
#print(sys.stdout.read()) # io.UnsupportedOperation: not readable
#print(sys.stderr.read()) # io.UnsupportedOperation: not readable

#print(sys.stdin.write('stdin.write')) # io.UnsupportedOperation: not writable
print(sys.stdout.write('stdout.write')) # stdout.write12
print(sys.stderr.write('stderr.write')) # 12\nstderr.write

