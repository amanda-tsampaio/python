print('Para o calculo de IMC, informe os seguintes dados:')
p = float(input('Peso(KG) = '))
h = float(input('Altura(M) = '))
IMC = p / (h**2)
if IMC < 18.5:
    print('Você está ABAIXO do peso')
elif (IMC >= 18.5 and IMC < 25):
    print('Você está com peso IDEAL')
elif IMC >= 25 and IMC < 30:
    print('Você está com SOBREPESO')
elif IMC >= 30 and IMC < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MORBIDA')