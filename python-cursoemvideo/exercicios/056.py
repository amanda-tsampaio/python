frase = str(input('Digite uma frase PALÍNDROMO = ')).strip().lower()
if frase.isalnum():
    print('Digite uma frase valida!!')
else:
    n = len(frase)
    #print(n)
    frase1 = ''
    for c in range(0, n):
        if frase[c].isalpha():
        #print(frase[c])
            frase1 = frase1 + frase[c]
    print(frase1)
    frase2 = frase1[::-1]
    print(frase2)
    if frase1 == frase2:
        print('Essa frase é PALINDROMO!!!')
    else:
        print('Essa frase NÃO É PALINDROMO!!!')




