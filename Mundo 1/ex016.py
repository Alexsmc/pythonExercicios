'''
Crie na tela um programa que leia um numero real qualquer
pelo teclado e ostre na tela a sua porção inteira

Ex: Digite um numero: 6.127
O numero 6.127 tem a sua parte inteira 6
'''

import math
n = float(input("Digite o numero real: "))
print('O Numero {} tem a sua parte inteira {}.'.format(n, math.trunc(n)))
