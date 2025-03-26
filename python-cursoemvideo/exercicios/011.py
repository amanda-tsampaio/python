import random
print('Digite os nomes dos alunos:')
a1: str = input('Aluno 1: ')
a2: str = input('Aluno 2: ')
a3: str = input('Aluno 3: ')
a4: str = input('Aluno 4: ')
lista = [a1, a2, a3, a4]
#aluno = random.choice(lista)
#apresentação = random.sample(lista, k=4)
#print(f'A pessoa sorteada para apagar o quadro é {aluno}')
print('A ordem de apresentação é:')
#print(f'{apresentação}')

random.shuffle(lista)
print(lista)









