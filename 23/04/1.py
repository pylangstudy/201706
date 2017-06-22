import random
rnd = random.random()
print(rnd)
print(int(rnd * 100)) # 0..100
print(random.randrange(2)) # 0..1
print(random.choice(['大吉', '中吉', '小吉', '末吉', '凶', '大凶']))
