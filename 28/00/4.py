from string import Template
t = Template('私の名前は$name_です。職業は${job}です。$$10で雇えます。')
print(t.substitute(name='山田'))
