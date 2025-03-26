inicio = int(input('PRIMEIRO NUM DA PA = '))
razao = int(input('RAZÃO DA PA = '))
cont = 1
mais = 10
while mais != 0:
    while cont != mais:
        print(f'{inicio}', end=' ')
        inicio += razao
        cont += 1
    print(' ')
    mais = int(input('Gostaria de mostrar mais quantos termos? '))
    cont = 0
print(' ')
print('FIM')

