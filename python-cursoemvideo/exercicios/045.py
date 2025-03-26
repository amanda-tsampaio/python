n1 = float(input('Digite a primeira nota = '))
n2 = float(input('Digite a segunda nota = '))
media = (n1+n2)/2
print(f'Sua média foi {media:.2f}!')
if media < 5:
    print('Voce foi REPROVADO!')
elif media >= 5 and media < 7:
    print('Voce precisa fazer RECUPERAÇÃO!')
else:
    print('Voce foi APROVADO!')