answer = [str(i) + '(アホ)' for i in range(1,20) if ( (0 == (i % 3)) or (0 < str(i).find(str(3))) )]
print(answer)
