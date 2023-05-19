'''
Crie um programa que leia 5 pesos
e mostre qual o maior peso e qual o menor
'''
maior = float(0)
menor = float(0)
pessoa_menor = int(0)
pessoa_maior = int(0)
for c in range(1,6):
    peso = float(input('Qual o peso da pessoa {}: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
        pessoa_menor = c
        pessoa_maior = c
    else:
        if peso > maior:
            maior = peso
            pessoa_maior = c
        elif peso < menor:
            menor = peso
            pessoa_menor = c
print('\nO maior peso é o da pessoa {}, Com {}kg.'.format(pessoa_maior,maior))
print('O menor peso é o da pessoa {}, com {}kg.'.format(pessoa_menor,menor))
