v = float(input('Por favor, informe o valor do produto = R$'))
print('=='*20)
print('''Digite 1 para pagamento À VISTA 
Digite 2 para pagamento no CARTÃO DE DEBITO 
Digite 3 para pagamento em 2X CARTÃO DE CRÉDITO  
Digite 4 para 3X OU MAIS CARTÃO DE CRÉDITO''')
print('=='*20)
p = int(input('Forma de pagamento = '))
if p == 1:
    print(f'O valor final do produto é {v*0.9} reais, COM 10% DE DESCONTO')
elif p == 2:
    print(f'O valor final do produto é {v*0.95} reais, COM 15% DE DESCONTO')
elif p == 3:
    print(f'O valor final do produto é {v} reais, SEM DESCONTO')
elif p == 4:
    n = int(input('Quantas parcelas gostaria de pagar?'))
    parcela = (v*1.2)/n
    print(f'O valor final do produto é {v*1.2} reais, COM 20% DE JUROS e PARCELAS de {parcela} reais')
else:
    print('Informe um valor válido!!')
