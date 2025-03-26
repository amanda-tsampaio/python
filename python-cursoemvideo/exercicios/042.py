n = int(input('Informe um numero inteiro: '))
print('''Qual base você gostaria de transformar esse numero inteiro?
Digite 1 para binario
Digite 2 para octal 
Digite 3 para hexadecimal''')
base = int(input('Base = '))
import math
if base == 1:
    print(f'O n {n} na base binaria é = {bin(n)[2:]}')
elif base == 2:
    print(f'O n {n} na base octal é = {oct(n)[2:]}')
elif base == 3:
    print(f'O n {n} na base hexadecimal é = {hex(n)[2:]}')
else:
    print('Digite um numero válido')
