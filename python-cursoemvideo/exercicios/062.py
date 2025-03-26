n = int(input('Fatorial de = '))
f = 1
while n != 1:
    f = f * n
    n = n - 1
    print(f'{n}', end=' ')
    print(' x ' if n > 1 else ' = ', end=' ')
print(f)
