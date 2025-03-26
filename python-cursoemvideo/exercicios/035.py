s = float(input('Digite seu salario: R$'))
if s > 1250.00:
    print(f'Você recebera um aumento de 10%, seu novo salario é de {s*1.1:.2f} reais')
else:
    print(f'Você recebera um aumento de 15%, seu novo salario é de {s*1.15:.2f} reais')