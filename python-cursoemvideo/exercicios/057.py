from datetime import date
ano = date.today().year
#print(ano)
a = 0
b = 0
for c in range(1, 4):
    ano1 = int(input(f'Digite o ano de nascimento da pessoa de num {c} = '))
    if ano1 > ano:
        b = b + 1
        print('Digite um num válido!')
    else:
        if ano - ano1 < 18:
            a = a + 1
print('-='*20)
print('Avaliando as informações válidas, temos  que:')
print(f'{a} MENOR(ES) DE IDADE e {3-a-b} MAIOR(ES) DE IDADE')

