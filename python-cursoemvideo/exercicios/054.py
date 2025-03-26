inicio = int(input('PRIMEIRO NUM DA PA = '))
razao = int(input('RAZÃO DA PA = '))
for c in range(inicio, 10*razao, razao):
    print(c, end=' ')
print('FIM')
