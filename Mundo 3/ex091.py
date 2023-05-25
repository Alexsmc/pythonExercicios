from random import randint
from time import sleep
jogador = {}
jogo = []

for c in range(4):
    jogador['O jogador'] = c+1
    jogador['tirou'] = randint(1,6)
    jogo.append(jogador.copy())

print('Valores Sorteados: ')
for e in jogo:
    for k,v in e.items():
        print(f'{k} {v}', end=' ')
    print()




'''
estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v)
'''
