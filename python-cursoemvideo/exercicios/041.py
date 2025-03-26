casa = float(input('Informe o valor da casa = R$'))
salario = float(input('Informe seu salario = R$'))
anos = int(input('Em quantos anos deseja pagar a casa? '))
parcela = (casa/anos)/12

if parcela > 0.3*salario:
    print('Desculpe, mas seu emprestimo foi negado, pois a parcela da casa excede 30% do seu salário. ')
else:
    print(f'Seu emprestimo foi aprovado e suas parcelas será de {parcela:.2f} reais.')

