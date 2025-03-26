n = int(input('Digite um num inteiro = '))
p1 = 0
p2 = 1
print(f'{p1} {p2}', end=' ')
while n != 2:
    f = p1 + p2
    print(f'{f}', end=' ')
    p1 = p2
    p2 = f
    n -= 1
print(' ')
print('FIM')