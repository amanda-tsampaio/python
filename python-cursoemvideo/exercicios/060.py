#s = str(input('Qual seu sexo [M/F]? ')).strip().upper()[0]
#while s not in 'MF':
#    s = str(input('Digite novamente uma resposta válida = '))
#print('Obrigada! resposta gravada com sucesso!')

import random
maquina = random.randint(0, 10)
humano = int(input('Advinhe qual num de 0 a 10 a maquina escolheu = '))
cont = 0
while maquina != humano:
    humano = int(input('Voce ERROU! Tente novamente = '))
    cont += 1
print('-='*20)
print(f'Você ACERTOU com {cont + 1} tentativa(s)!!')

