'''
Desenvolva um programa que leia 6 numeros inteiros
e mostre a soma apenas dos pares.
se o valor for ímpar desconsiderar
'''
soma = int(0)
for c in range(6):
    n = int(input('Digite um numero:'))
    if (n % 2) == 0:
        print('O numero {} é par. CONSIDERAR'.format(n))
        soma += n
    else:
        print('O Numero {} é ímpar. DESCONSIDERAR'.format(n))
print('\nA Soma de todos os números pares é: {}'.format(soma))
