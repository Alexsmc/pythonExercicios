'''
Escreva um programa que leia a velociade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.

A multa vai custar R$ 7,00 por cada KM acima do limite
'''

velocidade = int(input('Qual velocidade do carro? '))
multa = float((velocidade-80)*7)
if velocidade>80:
    print('Você foi multado em R$ {:.2f}'.format(multa))
else:
    print('Continue dirigindo assim!')