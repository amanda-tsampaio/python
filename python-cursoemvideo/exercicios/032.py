v = int(input('Digite com qual velocidade você passou na via: '))
print('A velocidade limite nessa via é de 80km/h ')
if v <= 80:
    print('Você não foi multado!')
else:
    print(f'Você ultrapassou o limite e será multado em {(v-80)*7} reais')