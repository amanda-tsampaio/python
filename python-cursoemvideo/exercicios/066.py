soma = cont = 0
opçao = 'S'
while opçao in 'Ss':
    n = int(input('Digite num inteiro = '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    opçao = str(input('Quer continuar [S/N] ? ')).strip().upper()
print(f'A media dos num digitados é igual {soma/cont:.2f}')
print(f'O maior num é igual a {maior}')
print(f'O menor num é igual a {menor}')
