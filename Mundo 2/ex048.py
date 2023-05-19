'''
A soma de todos os numero multiplos de 3 entre 1 e 500
'''
soma = int(0)
for c in range(0,501,3):
    print(c)
    soma += c
print('A soma total é: {}'.format(soma))