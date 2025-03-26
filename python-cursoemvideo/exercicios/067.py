cont = soma = 0
while True:
    n = int(input('Digite um num = '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} numeros e a soma é {soma}')