from random import randint

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
lista = (n1, n2, n3, n4, n5)
#maior = menor = 0
print(f'Os numeros sorteados  foram {lista}')
'''for c in range(0, len(lista)):
    # print(c)
    if c == 0 or lista[c] < menor:
        menor = lista[c]
    elif lista[c] > maior:
        maior = lista[c]'''
print(f'O maior Numero é: {max(lista)}')
print(f'O menor numero é: {min(lista)}')