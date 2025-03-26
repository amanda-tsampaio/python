print('Digite os comprimentos de três retas:')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r2 + r3 > r1 and r3 + r1 > r2 and r2 + r1 > r3:
    print('Esses valores formam um triangulo', end=' ')
    if r2 == r1 == r3:
        print('EQUILATERO!')
    elif (r2 == r1 and r2 != r3) or (r3 == r1 and r3 != r2) or (r3 == r2 and r3 != r1):
        print('ISOSCELES!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
else:
    print('Esses valores NÂO formam um triangulo')