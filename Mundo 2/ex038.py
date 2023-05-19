'''
Faça um progrmaa que comprar dois numeros e diz ql é o maior ou se são iguais
'''

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('O maior numero é {} e o menor {}'.format(num1, num2))
elif num2 > num1:
    print('O maior numero é {} e o menor é {}'.format(num2, num1))
else:
    print('Os numeros são iguais.')