'''
Faça um programa que leia o comprimenro do cateto
oposto adjacente da um triangulo, caucule e mostre o comprimenro
da hiponenusa
'''
import math
co = float(input('Digite o valor do cateto oposto'))
ca = float(input('Digite o valor do cateto adjacente '))
#hi = (co**2 + ca ** 2) **(1/2)
#print('A hipotenusa vale: {:.2f}'.format(hi))
hi = math.hypot(ca,co)
print('A hipotenusa vai medir: {:.2f}'.format(hi))