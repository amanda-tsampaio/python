ano1 = int(input('Olá, me informe seu ano de nascimento = '))
from datetime import date
data = date.today()
ano2 = data.year
#print(f'{ano2}')
idade = ano2 - ano1
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Sua classificação é MIRIM!')
elif idade <= 14:
    print('Sua classificação é INFANTIL!')
elif idade <= 19:
    print('Sua classificação é JUNIOR!')
elif idade <= 25:
    print('Sua classificação é SENIOR!')
elif idade > 25:
    print('Sua classificação é MASTER!')