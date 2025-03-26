n1 = float(input('Digite o primeiro valor = '))
n2 = float(input('Digite o segundo valor = '))
n = 0
print('-='*20)
while n != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    n = int(input('>>>>>>> Qual sua opção = '))
    if n == 1:
        print(f'A soma é igual a {n1 + n2}')
    if n == 2:
        print(f'A multiplicação é igual a {n1 * n2:.2f}')
    if n == 3:
        if n1 > n2:
            print(f'O maior numero é o primeiro = {n1}')
        elif n2 > n1:
            print(f'O maior numero é o segundo = {n2}')
        else:
            print(f'Os números sao iguais')
    if n == 4:
        n1 = float(input('Primeiro numero = '))
        n2 = float(input('Segundo numero = '))
    if n == 5:
        print('Finalizando...')
    else:
        print('Digite numeros validos!')
print('Programa finalizado com sucesso!!')