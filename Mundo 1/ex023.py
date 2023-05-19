print('''Faça um program que le um numero de 0-9999
e mostre na tela cada digito separado
Ex:
Digite um numero: 1834

Unidade: 4
Dezena: 3
centena 8
milhar 1''')

n = int(input('Digite um numero entre 0 e 9999: '))
while n != 0000:
    u = n // 1 % 10
    d = n // 10 % 10
    c = n // 100 % 10
    m = n // 1000 % 10
    print('Unidade: {}'.format(u))
    print('dezena: {}'.format(d))
    print('centena: {}'.format(c))
    print('milhar {}'.format(m))
    print('Digite 0000 para sair do programa.')
    n = int(input('Digite um numero entre 0 e 9999: '))
print('Fim do programa.')