from time import sleep
#for c in range(10, -1, -1):
#    print(c)
#    sleep(1)
#print('BUMMMM!')

#for c in range (1, 51):
 #   if c % 2 == 0:
  #      print(c, end=' ')
#print('FIM')
#for c in range (2, 51, 2):
 #       print(c, end=' ')
#print('FIM')

soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        #soma += c - mesma coisa
print(soma)
