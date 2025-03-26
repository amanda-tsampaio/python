n = int(input('Quantas pessoas você gostaria de avaliar o peso? '))
pesomaior = 0
pesomenor = 1000
for c in range (1, n+1):
    peso = float(input(f'Digite o peso(kg) da pessoa de num {c} = '))
    if peso > pesomaior:
        pesomaior = peso
    if peso < pesomenor:
        pesomenor = peso
print(f'O maior peso é {pesomaior} kg')
print(f'O menor peso é {pesomenor} kg')

