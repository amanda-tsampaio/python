cont = soma = n = 0
n = int(input('Digite num [999 p/ para] = '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite num [999 p/ para] = '))
print('-='*15)
print(f'Você digitou {cont} numeros')
print(f'A soma desses numeros é igual a {soma}')