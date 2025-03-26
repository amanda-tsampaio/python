n = int(input('Digite um numero inteiro = '))
print('-='*15)
soma = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        soma = soma + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\033[m')
if soma > 2:
    print('ESSE NUM NÃO É PRIMO')
else:
    print('ESSE NUM É PRIMO')
print('-='*15)