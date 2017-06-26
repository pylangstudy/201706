import json
import pprint
import sys
j = [{'name': 'Yamada', 'age': '100'}, {'name': 'Suzuki', 'age': '99'}, {'name': 'Tanaka', 'age': '88'}]
js = json.dumps(j)
print(js)
print('')
print(json.dumps(j, indent=4))
print('')

pprint.pprint(js)
print('')
pprint.pprint(js, compact=True)
print('')
pprint.pprint(js, width=-1, compact=True)
print('')
pprint.pprint(js, width=10000, compact=True)
print('')
pprint.pprint(js, width=30)
print('')
pprint.pprint(js, indent=4)
print('')
pp = pprint.PrettyPrinter(indent=4, width=sys.maxsize, depth=sys.maxsize, compact=True)
pp.pprint(js)
print('')
