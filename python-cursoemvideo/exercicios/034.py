ano = int(input('Digite um ano :'))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('Esse ano é bissexto!')
        else:
            print('Esse ano não é bissexto!')
    else:
        print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')


ano1 = int(input('Digite um ano :'))
if ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')

from datetime import date
hoje = int(input('Digite 0 para saber que ano é hoje'))
if hoje == 0:
    hoje = date.today().year
    print(f'O ano é {hoje}!')




