'''
desenvolva um progrmaa q leia o cumprimento de tres retas
e diga se eleas poram ou não fazer um triangulo
'''

r1 = int(input('Tamanho da reta 1: '))
r2 = int(input('tamanho da reta 2: '))
r3 = int(input('tamanho da reta 3: '))


def testa_eu():
    print('Testado')



testa_eu()

if (r2 + r1 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2):
    print('Esse triangulo é possível!')
else:
    print('Impossível formar triangulo!')


