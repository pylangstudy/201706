import json
with open('1.json', mode='w', encoding='utf-8') as f:
    d = {"key": "value"}
    json.dump(d, f)
with open('1.json', mode='r', encoding='utf-8') as f:
    d = json.load(f)
    print(d)

