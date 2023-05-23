lista = list()
repeat = 'Y'
while repeat in 'yY':
    num = int(input('Digite um numero: '))
    if num not in lista:
        print('Numero adicionado')
        lista.append(num)
    else:
        print('Numero duplicado. Não vou adicionar')
    repeat = str(input('Quer continuar? [Y/N] '))
    while repeat not in 'yYnN':
        repeat = str(input('Quer continuar? [Y/N] '))

lista.sort()
print(f'Os numeros digitatos foram: {lista}')