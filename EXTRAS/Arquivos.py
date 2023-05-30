from random import randint
import json
lista = list()
jogador = [0, 'nome']
with open('Valores.txt', 'r', encoding="utf-8") as arquivo:
    lista = json.load(arquivo)
print(lista)



while True:
    jogador[0] = randint(0,10)
    jogador[1] = str(input('Nome: '))
    lista.append(jogador[:])
    lista.sort(reverse=True)
    if len(lista)>10:
        lista.pop()
    resp = 'y'
    resp = str(input('Continuar? [S/N]: ')).strip()
    if resp in 'nN':
        break

with open('Valores.txt', 'w') as arquivo:
    json.dump(lista, arquivo)