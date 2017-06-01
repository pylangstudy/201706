squares = [x + 'は猫' + y + '。' for i,x in enumerate(['我輩', 'おいら', 'ミー']) for j,y in enumerate(['である', 'でやんす', 'ザマス']) if i==j]
print(squares)
