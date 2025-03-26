#tempo = int(input('Quantos anos tem seu carro? '))
#print('carro novo' if tempo <=3 else 'carro velho')
import random

n1 = int(input('Adivinhe o numero escolhido pele computador! \nDigite um numero de 0 a 5: '))
n2 = random.randint(0, 5)
print(f'O numero escolhido pelo computador foi {n2}')
if n1 == n2:
    print('PARABÉNS! Você acertou!')
else:
    print('Desculpe, você errou!')
