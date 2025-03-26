n = int(input('Digite o num de pessoas que voce gostaria de avaliar = '))
somaidade = 0
idadehomem = 0
nmulher = 0
for c in range(1, n+1):
    nome = str(input(f'Digite o nome da pessoa de num {c} = '))
    idade = int(input(f'Qual sua idade? '))
    sexo = str(input(f'Feminino ou masculino? '))
    somaidade += idade
    if sexo.lower() == 'masculino':
        if idade > idadehomem:
            idadehomem = idade
            nhomem = nome
    elif sexo.lower() == 'feminino':
        if idade < 20:
            nmulher += 1
mediaidade = somaidade/n
print('-='*20)
print(f'A média das idades é igual a {mediaidade:.1f} anos')
print('-='*20)
if idadehomem > 0:
    print(f'O homem mais velho é {nhomem} com {idadehomem} anos')
    print('-=' * 20)
elif idadehomem == 0:
    print(f'Não possui homem no grupo de pessoas.')
    print('-=' * 20)
elif nmulher > 0:
    print(f'Temos um total de {nmulher} mulher(es) com menos de 20 anos')
elif nmulher == 0:
    print(f'Não possui mulheres ou mulheres -20 anos no grupo de pessoas.')


