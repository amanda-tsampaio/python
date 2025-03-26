x = 0
print('=-' * 20)
n = int(input('Qual num você gostaria de ver a tabuada? '))
print('=-' * 20)
while True:
    while True:
        print(f'{x} x {n} = {x*n}')
        x += 1
        if x == 11:
            break
    print('=-' * 20)
    n = int(input('Qual num você gostaria de ver a tabuada? '))
    print('=-' * 20)
    x = 0
    if n < 0:
        break