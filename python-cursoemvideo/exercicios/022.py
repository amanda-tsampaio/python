n = input('Digite um numero de 0 a 9999: ')
if len(n) == 1:
    print(f'unidade: {n[1]}')
elif len(n) == 2:
    print(f'unidade: {n[1]} \ndezena: {n[0]}')
elif len(n) == 3:
    print(f'unidade: {n[2]} \ndezena: {n[1]} \ncentena: {n[0]}')
elif len(n) == 4:
    print(f'unidade: {n[3]} \ndezena: {n[2]} \ncentena: {n[1]} \nmilhar: {n[0]}')
else:
    print('Numero fora do intervalo!')

n = int(input('Digite um numero de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'unidade: {u} \ndezena: {d} \ncentena: {c} \nmilhar: {m}')

