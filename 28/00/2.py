from string import Template
t = Template('''名前: $name 職業: ${job} 所持: $item''')
print(t.safe_substitute(name='山田', job='勇者', item='薬草'))
print(t.safe_substitute(name='鈴木', job='戦士'))
print(t.safe_substitute(**{'name':'高橋', 'job':'魔女', 'item':'毒消し草'}))
monk = {'name':'吉本', 'job':'僧侶'}
print(t.safe_substitute(**monk))
