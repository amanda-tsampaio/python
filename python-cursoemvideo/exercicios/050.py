import random
from time import sleep
print('JO')
sleep(1)
print('GAN')
sleep(1)
print('DO!!')
sleep(1)
print('Olá! Vamos jogar pedra, papel e tesoura?')
print('''Estou pensando na minha resposta.... 
quando você falar a sua, falarei a minha automaticamente
Digite pedra, papel ou tesoura''')
print('-='*20)
jogo = ['pedra', 'papel', 'tesoura']
c = random.choice(jogo)
h = input('Resposta do jogador = ')
print(f'Resposta do computador = {c}')
print('-='*20)
if (c == 'pedra' and h == 'tesoura') or (c == 'tesoura' and h == 'papel') or (c == 'papel' and h == 'pedra'):
    print('AAH! Computador ganhou!!')
elif (h == 'pedra' and c == 'tesoura') or (h == 'tesoura' and c == 'papel') or (h == 'papel' and c == 'pedra'):
        print('POXA...O jogador ganhou!')
elif c == h:
    print('Ninguem ganhou!')
else:
    print('ERRO')
