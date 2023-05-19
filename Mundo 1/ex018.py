'''
Faça um programa que leia um angulo qualquer e mostre na
tela o valor do seno cosse e tangente desse angulo.
'''

import math
an = float(input('Digite um angulo:'))
co = math.cos(math.radians(an))
se = math.sin(math.radians(an))
tg = math.tan(math.radians(an))
print('O angulo {}° tem:\nseno {:.2f}°\nCosseno {:.2f}° e tangente {:.2f}°'.format(an, se, co, tg))