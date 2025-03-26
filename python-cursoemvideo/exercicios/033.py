n = int(input('Digite um numero inteiro: '))
if n % 2 == 0:
    print('Esse numero é par!')
else:
    print('Esse numero é impar!')

d = float(input('Digite quantos km será a viagem: '))
if d <= 200:
    print(f'O valor da passagem é de {d*0.50:.2f} reais')
else:
    print(f'O valor da passagem é de {d*0.45:.2f} reais')