from string import Template
t = Template('私の名前は$nameです。職業は${job}です。$$10で雇えます。')
print(t.substitute(name='山田', job='サラリーマン'))
print(t.substitute(name='鈴木', job='F1レーサー'))
t = Template('My name is$name. job is ${job}. please $$10.')
print(t.substitute(name='Yamada', job='***'))
print(t.substitute(name='Suzuki', job='???'))

