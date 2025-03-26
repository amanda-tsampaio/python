n = int(input('Qual numero você deseja ver a tabuada? '))
print('-='*20)
print(f'{' '*12}TABUADA DE {n}')
print('-='*20)
for c in range(0, 11):
    print(f'{c}  X  {n}  =  {n*c}')
print('-='*20)