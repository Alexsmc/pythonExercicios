lista = []
repeat = 'Y'
while repeat in 'yY':
    num = int(input('Digite um numero: '))
    for pos in range(0, len(lista)):
        if lista[pos] == num:
            print('Numero já adicionado')
        else:
            lista.append(num)
    repeat = str(input('Quer continuar? [Y/N] '))
    while repeat not in 'yYnN':
        repeat = str(input('Quer continuar? [Y/N] '))
lista.sort()
print(f'Os numeros digitatos foram: {lista}')