from datetime import date

ano = int(input('Digite o ano de seu nascimento = '))
data = date.today()
#print(f'{data}')
ano1 = data.year
#ano1 = date.today().year (faz sentido)
idade = ano1 - ano
#print(f'{ano}')
#print(f'{type(ano)}')
if idade < 18:
    print(f'Você ainda não pode se alistar, faltam {18 - idade} anos!')
elif idade == 18:
    print('Você está com idade de se alistar!')
elif idade > 18:
    print(f'Você perdeu o prazo pra se alistar, passaram {idade - 18} anos!')