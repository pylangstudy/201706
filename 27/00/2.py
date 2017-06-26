import pprint
import sys
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t)
print('')
pprint.pprint(t, compact=False)
print('')
pprint.pprint(t, width=-1, compact=True)
print('')
pprint.pprint(t, width=10000, compact=True)
print('')
pprint.pprint(t, width=30)
print('')
pprint.pprint(t, indent=4)
print('')
pp = pprint.PrettyPrinter(indent=4, width=sys.maxsize, depth=sys.maxsize, compact=True)
pp.pprint(t)
print('')
