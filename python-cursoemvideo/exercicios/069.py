import random
cont = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR!')
print('=-'*20)
while True:
    nmaquina = random.randint(0, 10)
    nhumano = int(input('Diga um valor = '))
    xhumano = str(input('Par ou impar [P/I]? ')).strip().upper()
    soma = nhumano + nmaquina
    if soma % 2 == 0:
        resposta = 'PAR'
    else:
        resposta = 'IMPAR'
    print(f'Voce jogou {nhumano} e o computador {nmaquina}. Total de {nhumano + nmaquina}. Deu {resposta} ')
    if resposta[0] != xhumano:
        print('Você perdeu!!')
        print('-='*20)
        print(f'GAME OVER! Voce venceu {cont} vezes!')
        break
    cont += 1

