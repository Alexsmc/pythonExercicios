'''
Escreva um programa que faça o computador "pensar" em um numero
entre 0 e 5 e peça que o usuário tente descobrir qual foi o numero
escolhido pelo computador.

O programa deverá dizer na tela se o usuário venceu ou perdeu
'''

import random

numero = random.randint(0, 5)

palpite = int(input("Advinhe o que estou pensando (Entre 0 e 5): "))

if numero != palpite:
    print("Erreou feio")
    print('meu o numero era: {}'.format(numero))
else:
    print('Acertou Mizeravi')

