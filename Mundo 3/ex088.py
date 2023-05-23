from time import sleep
from random import randint
numeros = 0
palpite = []

print('-'*40)
print('         JOGA NA MEGA SENA       ')
print('-'*40)
jogos = int(input('Quantos Jogos você quer que eu sorteie? '))
print('-='*3, f' SORTEANDO {jogos} JOGOS ', '=-'*3)
for i in range(jogos):
    while len(palpite) < 6:
        numeros = randint(1,60)
        if numeros not in palpite:
            palpite.append(numeros)
    palpite.sort()
    print(f'{i+1}ºPalpite: {palpite}')
    palpite.clear()
    sleep(0.8)
print('-='*5, ' BOA SORTE ', '=-'*5)