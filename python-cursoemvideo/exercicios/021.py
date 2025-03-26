nome = str(input('Digite seu nome completo :')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))
nome1 = nome.split()
print(nome1)
nome2 = ''.join(nome1)
print(nome2)
print(f'o numero de letras do nome completo é igual a {len(nome2)}')
print(f'o numero de letras do primeiro nome é igual a {len(nome1[0])}')




