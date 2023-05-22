lista = list()
repeat = 'Y'
while repeat in 'yY':
    num = int(input('Digite um numero: '))
    for p, v in enumerate(lista):
        if v == num:
            print('Numero já adicionado')
        else:
            lista.append(num)

    repeat = str(input('Quer continuar? [Y/N] '))
    while repeat not in 'yYnN':
        repeat = str(input('Quer continuar? [Y/N] '))

lista.sort()
print(f'Os numeros digitatos foram: {lista}')